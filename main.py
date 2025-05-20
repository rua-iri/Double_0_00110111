import logging
from uuid import uuid4
from double_0_00110111.constants import TEN_MB
from double_0_00110111.db_dao import DB_DAO
from double_0_00110111.helpers import (
    get_img_local, read_from_image, save_img_local
)
from double_0_00110111.tasks import process_image_encoding

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

    db_dao = DB_DAO()

    image_data = await file.read()

    # TODO save image to ./images/unencoded/ and store a record in the database
    file_location: str = save_img_local(
        filename=file.filename,
        subdir="unencoded",
        img_data=image_data
    )

    file_uuid = str(uuid4())
    file_uuid = uuid4().hex

    db_dao.insert_record(
        image_filename=file.filename,
        image_uuid=file_uuid,
        image_location=file_location
    )

    process_image_encoding.delay(
        image_uuid=file_uuid,
        user_message=message
    )

    return {
        "Image Process": "Encode",
        "status": "Processing",
        "uuid": file_uuid,
    }


@app.post("/decode")
async def decode(file: UploadFile):

    if file.size > TEN_MB:
        raise HTTPException(status_code=403, detail="Image Size Too Large")

    image_data: bytes = await file.read()

    # TODO read from database and fetch image

    image_response = read_from_image(image_data)

    return {
        "Image Process": "Decode",
        "status": image_response.get("status"),
        "message": image_response.get("message"),
    }


@app.get(
    "/image/{img_uuid}",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response
)
def get_encoded_image(img_uuid: str):
    """
    Retrieve the encoded image for the user from s3
    using the filename passed via the URL
    """

    img_data = get_img_local(img_uuid, "encoded")

    if not img_data:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(
        content=img_data,
        media_type="image/png"
    )
