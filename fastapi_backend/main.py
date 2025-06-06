import logging
from uuid import uuid4
from double_0_00110111.constants import TEN_MB
from double_0_00110111.db_dao import DB_DAO
from double_0_00110111.helpers import (
    generate_filename, get_img_local,
    read_message_from_image, sanitise_filename,
    save_img_local
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

    if file.size and file.size > TEN_MB:
        raise HTTPException(status_code=403, detail="Image Size Too Large")

    db_dao = DB_DAO()

    image_data = await file.read()

    file_uuid = uuid4().hex

    if file.filename:
        filename_sanitised: str = sanitise_filename(file.filename)
    else:
        filename_sanitised: str = "image.png"

    filename_unique = generate_filename(filename_sanitised, file_uuid)

    file_location: str = save_img_local(
        filename=filename_unique,
        subdir="unencoded",
        img_data=image_data
    )

    db_dao.insert_record(
        image_filename=filename_unique,
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

    if file.size and file.size > TEN_MB:
        raise HTTPException(status_code=403, detail="Image Size Too Large")

    image_data: bytes = await file.read()

    image_response = read_message_from_image(image_data)

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
    """Retrieve the encoded image for the user from storage
    using the filename passed via the URL

    Args:
        img_uuid (str): The uuid identifying the image
        record in the database

    Raises:
        HTTPException: 404 image not found

    Returns:
        Response: A FastAPI response containing the image content
    """

    db_dao = DB_DAO()
    image_record = db_dao.select_record_by_uuid(img_uuid)

    if not image_record:
        raise HTTPException(status_code=404, detail="Image not found")

    if not image_record.get("is_processed"):
        return Response(
            status_code=202,
            content={"detail": "Image not yet ready"}
        )

    filepath: str = f"/images/encoded/{image_record.get('image_filename')}"

    img_data = get_img_local(filepath)

    return Response(
        content=img_data,
        media_type="image/png"
    )
