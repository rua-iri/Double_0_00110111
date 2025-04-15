import logging
from double_0_00110111.constants import TEN_MB
from double_0_00110111.helpers import (
    read_from_image, retrieve_img_s3, write_to_image
)

from fastapi import FastAPI, Form, HTTPException, Response, UploadFile
from typing import Annotated


app = FastAPI()


logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


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

    image_data: bytes = await file.read()

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

    img_data = retrieve_img_s3(img_filename)

    if not img_data:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(
        content=img_data,
        media_type="image/png"
    )
