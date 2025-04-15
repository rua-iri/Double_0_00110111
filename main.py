from uuid import uuid4
from PIL import Image
import logging
import io
from double_0_00110111 import helpers
from double_0_00110111.constants import XML_START, XML_END, TEN_MB

from fastapi import FastAPI, Form, HTTPException, Response, UploadFile
from typing import Annotated


app = FastAPI()


logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


# function to encode message in a given image
def write_to_image(image_data: bytes, messageText: str) -> dict:
    try:
        img: Image = Image.open(io.BytesIO(image_data))
        file_format = img.format

        if img.mode != "RGB":
            img = img.convert("RGB")

        imgWidth, imgHeight = img.size
        imgPixels: list = list(img.getdata())

        if not helpers.is_valid_file_format(file_format):
            raise HTTPException(status_code=400, detail="Image file invalid")

        binMessage: str = ""
        for letter in messageText:
            binMessage += format(ord(letter), "08b")

        binImgData: str = ""
        for px in imgPixels:
            binImgData += bin(px[0])[-1] + bin(px[1])[-1] + bin(px[2])[-1]

        if helpers.is_image_already_encoded(binImgData, binMessage):
            raise HTTPException(
                status_code=400,
                detail="Image or message have already been encoded"
            )

        binMessage = XML_START + binMessage + XML_END

        if not helpers.isImgLongEnough(binMessage, imgWidth, imgHeight):
            raise HTTPException(
                status_code=400, detail="Image too small to contain message"
            )

        logger.info("Image meets requirements")

        requiredPixels = len(binMessage) // 3 + 1

        encodeLocation: int = helpers.get_encode_location(
            requiredPixels, len(imgPixels)
        )

        logger.info("Initiating pixel modification")

        imgPixels = helpers.encode_image(
            encodeLocation, requiredPixels, imgPixels, binMessage
        )

        img.putdata(imgPixels)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        object_key = f"{uuid4().hex}.png"

        helpers.save_img_s3(object_key, img_bytes)

        return {
            "status": "success",
            "url": object_key
        }

    except Exception as e:
        logger.error(e)
        raise e


# function to extract secret message from a file
def read_from_image(image_data) -> dict:
    try:
        img: Image = Image.open(io.BytesIO(image_data))
        file_format = img.format

        if img.mode != "RGB":
            img = img.convert("RGB")

        img_pixels: list = list(img.getdata())

        if not helpers.is_valid_file_format(file_format):
            raise HTTPException(status_code=400, detail="Image file invalid")

        # concatenate the data from the least significant bit of every pixel
        binaryData: str = ""
        for px in img_pixels:
            binaryData += bin(px[0])[-1] + bin(px[1])[-1] + bin(px[2])[-1]

        # find the start and the end using the binary values for the xml tags
        msg_start_location: int = binaryData.find(XML_START) + len(XML_START)
        msg_end_location: int = binaryData.find(XML_END)

        if msg_end_location == -1:
            raise HTTPException(status_code=400, detail="Image Not Encoded")

        msg_text: str = helpers.decode_image(
            msg_start_location, msg_end_location, binaryData
        )

        return {"status": "success", "message": msg_text}

    except Exception as e:
        logger.error(e)


@app.get("/hello")
async def hello_world():
    """
    Hello World Endpoint for testing purposes
    """
    return {"Hello": "World"}


@app.post("/encode")
async def encode(
    message: Annotated[str, Form()],
    file: UploadFile,
):

    if file.size > TEN_MB:
        raise HTTPException(status_code=403, detail="Image Size Too Large")

    image_data = await file.read()
    image_response = write_to_image(image_data=image_data, messageText=message)

    return {
        "Image Process": "Encode",
        "status": image_response.get("status"),
        "url": image_response.get("url"),
    }


@app.post("/decode")
async def decode(file: UploadFile):

    if file.size > TEN_MB:
        raise HTTPException(status_code=403, detail="Image Size Too Large")

    image_data = await file.read()

    image_response = read_from_image(image_data)

    return {
        "Image Process": "Encode",
        "status": image_response.get("status"),
        "message": image_response.get("message"),
    }


@app.get(
    "/image/{img_filename}",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response
)
def get_encoded_image(img_filename: str):
    """
    Retrieve the encoded image for the user from s3
    using the filename passed via the URL
    """

    img_data = helpers.retrieve_img_s3(img_filename)

    if not img_data:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(
        content=img_data,
        media_type="image/png"
    )
