

from celery import Celery
import time
import os

from double_0_00110111.db_dao import DB_DAO
from double_0_00110111.helpers import get_img_local, write_to_image

app = Celery(
    "tasks",
    broker=os.getenv("queue_conn_string")
)


@app.task
def add(x, y):
    time.sleep(3)
    print(x+y)
    return x+y


@app.task
def process_image_encoding(image_uuid: str, user_message: str):
    db_dao = DB_DAO()
    result = db_dao.select_record_by_uuid(image_uuid)

    full_image_path: str = result.get("image_location")
    full_image_path += result.get("image_filename")
    image_data: bytes = get_img_local(full_image_path)

    write_to_image(
        image_data=image_data,
        messageText=user_message
    )

    db_dao.update_image_processed_status(image_uuid)
    return result


@app.task
def decode_image(image_uuid: str): pass
