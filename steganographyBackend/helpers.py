from cgi import FieldStorage
import io
import os
# import boto3


# s3_client = boto3.client("s3")
# ProcessedImageBucket = os.getenv("ProcessedImageBucket")

def parse_form_data(event: dict) -> tuple:
    try:
        body = io.BytesIO(bytes(event['body'], "utf-8"))

        # load body into FieldStorage object
        field_storage = FieldStorage(
            fp=body,
            environ={
                "REQUEST_METHOD": "POST",
                "CONTENT_TYPE": event['headers']['Content-Type'],
                "CONTENT_LENGTH": body.getbuffer().nbytes
            },
            keep_blank_values=True
            )

        form_inputs = {}
        files = {}

        # iterate through each field and store in relevant dict
        for field in field_storage.list:
            if field.filename:
                files[field.name] = {
                    "filename": field.filename,
                    "value": field.value,
                    "content_type": field.type
                }
            else:
                form_inputs[field.name] = field.value

        return (
            form_inputs.get("operation"), 
            form_inputs.get("message"), 
            files.get("image")
            )

        
    except Exception as e:
        raise e




def put_image_s3(image_data: bytes, object_key: str) -> str:
    try:
        s3_client.upload_fileobj(image_data, ProcessedImageBucket, object_key)
        return f"https://{ProcessedImageBucket}.s3.amazonaws.com/{object_key}"

    except Exception as e:
        raise e

