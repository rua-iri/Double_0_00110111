from double_0_00110111.constants import LOREM_MESSAGE
from double_0_00110111.helpers import write_to_image


from fastapi import HTTPException


import re
import unittest


class TestWriteToImage(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self):
        return super().setUp()

    def test_write_success(self):
        expected_val = {
            "status": "success",
            "url": "9545a140951246ae8f253b805c946500.png",
        }

        with open("sample_images/sample.png", "rb") as file:
            file_data = file.read()

        actual_val = write_to_image(file_data, "Test Message")

        regex_search_result = re.search(
            "^[a-zA-Z0-9]{32}.png$", actual_val["url"])

        self.assertEqual(expected_val["status"], actual_val["status"])
        self.assertEqual(type(regex_search_result), re.Match)

        object_key = actual_val.get("url")

        file_path = f"images/encoded/{object_key}"
        file = open(file_path, "rb")
        file.read()
        file.close()

    def test_write_invalid_format(self):
        expected_val = HTTPException(
            status_code=400, detail="Image file invalid")

        with open("sample_images/sample.jpg", "rb") as file:
            file_data = file.read()

        with self.assertRaises(HTTPException) as context:
            write_to_image(file_data, "Test Message")

        actual_exception = context.exception

        self.assertEqual(
            actual_exception.status_code,
            expected_val.status_code
        )
        self.assertEqual(
            actual_exception.detail,
            expected_val.detail
        )

    def test_write_image_already_encoded(self):
        expected_val = HTTPException(
            status_code=400,
            detail="Image or message have already been encoded"
        )

        with open("sample_images/sample_encoded.png", "rb") as file:
            file_data = file.read()

        with self.assertRaises(HTTPException) as context:
            write_to_image(file_data, "Test Message")

        actual_exception = context.exception

        self.assertEqual(
            actual_exception.status_code,
            expected_val.status_code
        )
        self.assertEqual(
            actual_exception.detail,
            expected_val.detail
        )

    def test_write_message_already_encoded(self):
        expected_val = HTTPException(
            status_code=400,
            detail="Image or message have already been encoded"
        )

        with open("sample_images/sample.png", "rb") as file:
            file_data = file.read()

        with self.assertRaises(HTTPException) as context:
            write_to_image(file_data, "<msg>Test Message</msg>")

        actual_exception = context.exception

        self.assertEqual(
            actual_exception.status_code,
            expected_val.status_code
        )
        self.assertEqual(
            actual_exception.detail,
            expected_val.detail
        )

    def test_write_message_too_long(self):
        expected_val = HTTPException(
            status_code=400, detail="Image too small to contain message"
        )

        with open("sample_images/sample_favicon.png", "rb") as file:
            file_data = file.read()

        with self.assertRaises(HTTPException) as context:
            write_to_image(file_data, LOREM_MESSAGE)

        actual_exception = context.exception

        self.assertEqual(
            actual_exception.status_code,
            expected_val.status_code
        )
        self.assertEqual(
            actual_exception.detail,
            expected_val.detail
        )