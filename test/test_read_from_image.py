import unittest
from double_0_00110111.helpers import read_from_image
from fastapi import HTTPException


class TestReadFromImage(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_read_success(self):
        expected_val = {
            "status": "success",
            "message": "I am putting a secret message at a random location",
        }

        with open("sample_images/sample_encoded.png", "rb") as file:
            file_data = file.read()

        self.assertEqual(expected_val, read_from_image(file_data))

    def test_read_not_encoded(self):
        expected_val = HTTPException(
            status_code=400, detail="Image Not Encoded")

        with open("sample_images/sample.png", "rb") as file:
            file_data = file.read()

        with self.assertRaises(HTTPException) as context:
            read_from_image(file_data)

        actual_exception = context.exception

        self.assertEqual(
            expected_val.status_code,
            actual_exception.status_code
        )
        self.assertEqual(
            expected_val.detail,
            actual_exception.detail
        )

    def test_read_invalid_format(self):
        expected_val = HTTPException(
            status_code=400, detail="Image file invalid")

        with open("sample_images/sample.jpg", "rb") as file:
            file_data = file.read()

        with self.assertRaises(HTTPException) as context:
            read_from_image(file_data)

        actual_exception = context.exception
        # self.assertRaises(HTTPException)
        self.assertEqual(
            expected_val.status_code,
            actual_exception.status_code
        )
        self.assertEqual(
            expected_val.detail,
            actual_exception.detail
        )


if __name__ == "__main__":
    unittest.main()
