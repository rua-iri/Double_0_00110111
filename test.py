

from main import read_from_image
from fastapi import HTTPException


def test_read_from_image():
    expected_val = {"status": "success", "message": "I am putting a secret message at a random location"}

    with open("testImages/testImage_encoded.png", "rb") as file:
        file_data = file.read()
        
    assert expected_val == read_from_image(file_data)



def test_read_from_image_not_encoded():
    expected_val =  HTTPException(status_code=400, detail="Image Not Encoded")

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




if __name__ == "__main__":
    test_read_from_image()
    test_read_from_image_not_encoded()
    test_read_from_image_invalid_format()

