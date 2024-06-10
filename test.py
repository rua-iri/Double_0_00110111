from main import write_to_image, read_from_image
from constants import LOREM_MESSAGE
from fastapi import HTTPException
import re
from tqdm import tqdm



def test_read_from_image():
    expected_val = {
        "status": "success",
        "message": "I am putting a secret message at a random location",
    }

    with open("testImages/testImage_encoded.png", "rb") as file:
        file_data = file.read()

    assert expected_val == read_from_image(file_data)


def test_read_from_image_not_encoded():
    expected_val = HTTPException(status_code=400, detail="Image Not Encoded")

    with open("testImages/testImage.png", "rb") as file:
        file_data = file.read()

    actual_val = read_from_image(file_data)

    assert expected_val.status_code == actual_val.status_code
    assert expected_val.detail == actual_val.detail


def test_read_from_image_invalid_format():

    expected_val = HTTPException(status_code=400, detail="Image file invalid")

    with open("testImages/testImage.jpg", "rb") as file:
        file_data = file.read()

    actual_val = read_from_image(file_data)

    assert expected_val.status_code == actual_val.status_code
    assert expected_val.detail == actual_val.detail


def test_write_to_image():
    expected_val = {
        "status": "success",
        "url": f"/image/9545a140951246ae8f253b805c946500.png",
    }

    with open("testImages/testImage.png", "rb") as file:
        file_data = file.read()

    actual_val = write_to_image(file_data, "Test Message")

    regex_search_result = re.search("^/image/.{32}.png$", actual_val["url"])

    assert expected_val["status"] == actual_val["status"]
    assert type(regex_search_result) == re.Match


def test_write_to_image_invalid_format():
    expected_val = HTTPException(status_code=400, detail="Image file invalid")

    with open("testImages/testImage.jpg", "rb") as file:
        file_data = file.read()

    actual_val: HTTPException = write_to_image(file_data, "Test Message")

    assert actual_val.status_code == expected_val.status_code
    assert actual_val.detail == expected_val.detail


def test_write_to_image_image_encoded():
    expected_val = HTTPException(
        status_code=400, detail="Image or message have already been encoded"
    )

    with open("testImages/testImage_encoded.png", "rb") as file:
        file_data = file.read()

    actual_val: HTTPException = write_to_image(file_data, "Test Message")

    assert actual_val.status_code == expected_val.status_code
    assert actual_val.detail == expected_val.detail


def test_write_to_image_message_encoded():
    expected_val = HTTPException(
        status_code=400, detail="Image or message have already been encoded"
    )

    with open("testImages/testImage.png", "rb") as file:
        file_data = file.read()

    actual_val: HTTPException = write_to_image(file_data, "<msg>Test Message</msg>")

    assert actual_val.status_code == expected_val.status_code
    assert actual_val.detail == expected_val.detail


def test_write_to_image_long_message():
    expected_val = HTTPException(status_code=400, detail="Image too small to contain message")

    with open("testImages/testImage_favicon.png", "rb") as file:
        file_data = file.read()

    actual_val: HTTPException = write_to_image(file_data, LOREM_MESSAGE)

    assert actual_val.status_code == expected_val.status_code
    assert actual_val.detail == expected_val.detail





if __name__ == "__main__":
    p_bar: tqdm = tqdm(total=8, desc="Running tests")
    p_bar.colour = "green"

    try:
        test_read_from_image()
        p_bar.update(1)
        test_read_from_image_not_encoded()
        p_bar.update(1)
        test_read_from_image_invalid_format()
        p_bar.update(1)
        test_write_to_image()
        p_bar.update(1)
        test_write_to_image_invalid_format()
        p_bar.update(1)
        test_write_to_image_image_encoded()
        p_bar.update(1)
        test_write_to_image_message_encoded()
        p_bar.update(1)
        test_write_to_image_long_message()
        p_bar.update(1)

        p_bar.close()
        print("All Tests Pass")
    
    except Exception as e:
        p_bar.colour = "red"
        print(e)
        p_bar.close()

    

    
