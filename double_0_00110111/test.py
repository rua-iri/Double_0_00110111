import unittest
from main import write_to_image, read_from_image
from constants import LOREM_MESSAGE
from fastapi import HTTPException
import re


class TestReadFromImage(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_read_success(self):
        expected_val = {
            "status": "success",
            "message": "I am putting a secret message at a random location",
        }

        with open("../sample_images/sample_encoded.png", "rb") as file:
            file_data = file.read()

        self.assertEqual(expected_val, read_from_image(file_data))

    def test_read_not_encoded(self):
        expected_val = HTTPException(
            status_code=400, detail="Image Not Encoded")

        with open("../sample_images/sample.png", "rb") as file:
            file_data = file.read()

        actual_val = read_from_image(file_data)

        self.assertEqual(expected_val.status_code, actual_val.status_code)
        self.assertEqual(expected_val.detail, actual_val.detail)

    def test_read_invalid_format(self):
        expected_val = HTTPException(
            status_code=400, detail="Image file invalid")

        with open("../sample_images/sample.jpg", "rb") as file:
            file_data = file.read()

        actual_val = read_from_image(file_data)

        self.assertEqual(expected_val.status_code, actual_val.status_code)
        self.assertEqual(expected_val.detail, actual_val.detail)


class TestWriteToImage(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_write_success(self):
        expected_val = {
            "status": "success",
            "url": "9545a140951246ae8f253b805c946500.png",
        }

        with open("../sample_images/sample.png", "rb") as file:
            file_data = file.read()

        actual_val = write_to_image(file_data, "Test Message")

        regex_search_result = re.search(
            "^[a-zA-Z0-9]{32}.png$", actual_val["url"])

        self.assertEqual(expected_val["status"], actual_val["status"])
        self.assertEqual(type(regex_search_result), re.Match)

        # TODO: rewrite below code to check if the file exists in
        # s3 bucket not in local storage

        # if does_file_exist(file_location):
        #     del_file(file_location)
        # else:
        #     raise Exception("Encoded File Not Found")

    def test_write_invalid_format(self):
        expected_val = HTTPException(
            status_code=400, detail="Image file invalid")

        with open("../sample_images/sample.jpg", "rb") as file:
            file_data = file.read()

        actual_val: HTTPException = write_to_image(file_data, "Test Message")

        self.assertEqual(actual_val.status_code, expected_val.status_code)
        self.assertEqual(actual_val.detail, expected_val.detail)

    def test_write_image_already_encoded(self):
        expected_val = HTTPException(
            status_code=400,
            detail="Image or message have already been encoded"
        )

        with open("../sample_images/sample_encoded.png", "rb") as file:
            file_data = file.read()

        actual_val: HTTPException = write_to_image(file_data, "Test Message")

        self.assertEqual(actual_val.status_code, expected_val.status_code)
        self.assertEqual(actual_val.detail, expected_val.detail)

    def test_write_message_already_encoded(self):
        expected_val = HTTPException(
            status_code=400,
            detail="Image or message have already been encoded"
        )

        with open("../sample_images/sample.png", "rb") as file:
            file_data = file.read()

        actual_val: HTTPException = write_to_image(
            file_data, "<msg>Test Message</msg>")

        self.assertEqual(actual_val.status_code, expected_val.status_code)
        self.assertEqual(actual_val.detail, expected_val.detail)

    def test_write_message_too_long(self):
        expected_val = HTTPException(
            status_code=400, detail="Image too small to contain message"
        )

        with open("../sample_images/sample_favicon.png", "rb") as file:
            file_data = file.read()

        actual_val: HTTPException = write_to_image(file_data, LOREM_MESSAGE)

        self.assertEqual(actual_val.status_code, expected_val.status_code)
        self.assertEqual(actual_val.detail, expected_val.detail)


if __name__ == "__main__":
    unittest.main()
