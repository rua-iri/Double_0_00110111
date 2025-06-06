

from celery import Celery
import time
import os
import logging

from double_0_00110111.db_dao import DB_DAO
from double_0_00110111.helpers import get_img_local, write_message_to_image

app = Celery(
    "tasks",
    broker=os.getenv("queue_conn_string")
)

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


@app.task
def add(x, y):
    time.sleep(3)
    print(x+y)
    return x+y


@app.task
def process_image_encoding(image_uuid: str, user_message: str):
    db_dao = DB_DAO()
    image_record = db_dao.select_record_by_uuid(image_uuid)

    logging.info(f"image_uuid: {image_uuid}")
    logging.info(f"user_message: {user_message}")

    full_image_path: str = "/images/unencoded/"
    full_image_path += image_record.get("image_filename")

    image_data: bytes = get_img_local(full_image_path)

    write_message_to_image(
        image_data=image_data,
        messageText=user_message,
        image_filename=image_record.get("image_filename")
    )

    db_dao.update_image_processed_status(
        image_uuid=image_uuid
    )
    return image_record


@app.task
def decode_image(image_uuid: str): pass
