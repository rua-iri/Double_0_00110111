from constants import XML_START, XML_END
import random
from PIL import Image


# check if image is large enough to store message
def isImgLongEnough(msg: str, wdth: int, hght: int) -> bool:
    """Checks that the image contains the minimum number of pixels

    Args:
        msg (str): The message to be encoded
        wdth (int): The image's width in pixels
        hght (int): The image's height in pixels

    Returns:
        bool: Whether the image is long enough
    """

    if (len(msg) // 3 + 1) < (wdth * hght):
        return True
    else:
        return False


def is_image_already_encoded(binary_img_data: str, binary_message: str) -> bool:
    """Checks that the image has not already been encoded with
    a message by this program and that the message does not include
    the XML tags used to denote the beginning and end of a message

    Args:
        binary_img_data (str): The binary data from the image
        binary_message (str): The message to be encoded in binary

    Raises:
        Exception: The message contains the XML tags
        Exception: The image has been encoded previously

    Returns:
        bool: Whether the image and message are invalid
    """

    if XML_START in binary_img_data or XML_END in binary_img_data:
        raise Exception("Invalid Message")
    if XML_START in binary_message or XML_END in binary_message:
        raise Exception("Image written to previously")

    return False


# get random location in the image to encode the message
def get_encode_location(reqPixels: int, maxPixels: int) -> int:
    """Finds a random location in the file to encode the message

    Args:
        reqPixels (int): The number of pixels required for the message
        maxPixels (int): The total number of pixels in the image

    Returns:
        int: _description_
    """
    encodeLocation = random.randint(0, (maxPixels - reqPixels))

    # regenerate encodeLocation until it is divisible by 8
    while encodeLocation % 8:
        encodeLocation = random.randint(0, (maxPixels - reqPixels))

    return encodeLocation


def save_encoded_image(img_name, img_data):
    """Saves the modified image to the server

    Args:
        img_name (_type_): The filename to which the image will be saved
        img_data (_type_): The binary data of the image file

    Raises:
        e: An exception which could arise while saving the file
    """
    img_location = f"encoded/{img_name}"
    try:
        with open(img_location, "wb") as img_file:
            img_file.write(img_data)

    except Exception as e:
        raise e


def encode_image(
    encode_location: int, required_pixels: int, image_pixels: list, binary_message: str
) -> list:
    """
    Handles the encoding of a message into the binary data of the image
    by modifying the least significant bit

    Args:
        encode_location (int): The start location where the message should begin
        required_pixels (int): The number of pixels which should be modified
        image_pixels (list): A list containing the rgb values of every pixel in the image
        binary_message (str): The message to be encoded, converted into binary

    Returns:
        list: A modified version of the image_pixels list which now contains the binary_message
    """

    binary_index = 0
    # iterate through each pixel to be modified
    for pixelIndex in range(encode_location, (encode_location + required_pixels)):
        # convert to list to make mutable
        image_pixels[pixelIndex] = list(image_pixels[pixelIndex])

        # iterate through each colour value for each pixel
        for colourIndex in range(len(image_pixels[pixelIndex])):
            if binary_index < len(binary_message):

                image_pixels[pixelIndex][colourIndex] = int(
                    bin(image_pixels[pixelIndex][colourIndex])[:-1]
                    + binary_message[binary_index],
                    2,
                )

                binary_index += 1

        # convert back to tuple
        image_pixels[pixelIndex] = tuple(image_pixels[pixelIndex])

    return image_pixels


def decode_image(
    msg_start_location: int, msg_end_location: int, binary_data: str
) -> str:
    """Decodes the message from the image

    Args:
        msg_start_location (int): The location where the message begins
        msg_end_location (int): The location where the message ends
        binary_data (str): The binary data from the least significant bit of every pixel

    Returns:
        str: The text encoded in the image
    """
    
    # decode binary into readable text
    totalText: str = ""
    for i in range((msg_start_location // 8), (msg_end_location // 8)):
        charStart: int = i * 8
        charEnd: int = (i + 1) * 8
        totalText += chr(int(binary_data[charStart:charEnd], 2))

    return totalText


def is_valid_file(image: Image):

    if image.format != "PNG":
        return False

    if image.size
    # TODO: implement file validation here
    
    return True
