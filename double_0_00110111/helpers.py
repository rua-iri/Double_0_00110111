import io
from uuid import uuid4
from PIL import Image

from double_0_00110111 import helpers
import logging
from fastapi import HTTPException
from .constants import XML_START, XML_END
import random


logger = logging.getLogger(__name__)


def is_img_long_enough(msg: str, wdth: int, hght: int) -> bool:
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


def is_image_already_encoded(
        binary_img_data: str,
        binary_message: str) -> bool:
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
        return True
    if XML_START in binary_message or XML_END in binary_message:
        return True

    return False


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


def encode_image(
    encode_location: int,
    required_pixels: int,
    image_pixels: list,
    binary_message: str
) -> list:
    """
    Handles the encoding of a message into the binary data of the image
    by modifying the least significant bit

    Args:
        encode_location (int): The start location where
            the message should begin
        required_pixels (int): The number of pixels which
            should be modified
        image_pixels (list): A list containing the rgb values
            of every pixel in the image
        binary_message (str): The message to be encoded, converted into binary

    Returns:
        list: A modified version of the image_pixels list
            which now contains the binary_message
    """

    binary_index = 0
    # iterate through each pixel to be modified
    min_pix_index = encode_location
    max_pix_index = (encode_location + required_pixels)

    for pixelIndex in range(min_pix_index, max_pix_index):
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
        binary_data (str): The binary data from the least
            significant bit of every pixel

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


def is_valid_file_format(file_format: str):

    if file_format != "PNG":
        return False

    return True


def encrypt_message(message: str) -> str:
    message_encrypted = message
    return message_encrypted


def save_img_local(filename: str, subdir: str, img_data: str) -> str:
    """Save an image file locally in the /images/ directory

    Args:
        filename (str): The name that the object should be saved as
        img_data (str): The binary image data that should
        be written to the object
    """
    file_location: str = f"/images/{subdir}/{filename}"

    with open(file_location, 'wb') as file:
        file.write(img_data)

    return file_location


def get_img_local(filepath: str) -> bytes:
    """Retrieve an encoded image from the local directory

    Args:
        filename (str): The name of the file to the retrieved

    Returns:
        _type_: The bytes of the image being retrieved
    """

    with open(filepath, "rb") as file:
        return file.read()


def read_from_image(image_data: bytes) -> dict:
    """Handle the image data passed from the API endpoint
    and extract the text encoded in it

    Args:
        image_data (bytes): The bytes data loaded from the image

    Raises:
        HTTPException: The image is not in the correct format
        HTTPException: The image has not been encoded with a message
        HTTPException: A generic exception to handle other cases

    Returns:
        dict: The Response status and message contained within the message
    """
    try:
        img: Image = Image.open(io.BytesIO(image_data))
        file_format = img.format

        if img.mode != "RGB":
            img = img.convert("RGB")

        img_pixels: list = list(img.getdata())

        if not helpers.is_valid_file_format(file_format):
            raise HTTPException(status_code=400, detail="Image file invalid")

        # concatenate the data from the least significant bit of every pixel
        binaryData: str = ""
        for px in img_pixels:
            binaryData += bin(px[0])[-1] + bin(px[1])[-1] + bin(px[2])[-1]

        # find the start and the end using the binary values for the xml tags
        msg_start_location: int = binaryData.find(XML_START) + len(XML_START)
        msg_end_location: int = binaryData.find(XML_END)

        if msg_end_location == -1:
            raise HTTPException(status_code=400, detail="Image Not Encoded")

        msg_text: str = helpers.decode_image(
            msg_start_location, msg_end_location, binaryData
        )

        return {"status": "success", "message": msg_text}

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")


def write_to_image(image_data: bytes, messageText: str) -> dict:
    """Write the secret message to the image and store it

    Args:
        image_data (bytes): The bytes data of the image file
        messageText (str): The secret message to be encoded

    Raises:
        HTTPException: An image of an invalid format has been sent
        HTTPException: The image has already been encoded with a message
        HTTPException: The image is not large enough to contain
        the secret message
        HTTPException: A generic exception to handle other cases

    Returns:
        dict: The status of the upload and the object's key in s3
    """
    try:
        img: Image = Image.open(io.BytesIO(image_data))
        file_format = img.format

        if img.mode != "RGB":
            img = img.convert("RGB")

        imgWidth, imgHeight = img.size
        imgPixels: list = list(img.getdata())

        if not is_valid_file_format(file_format):
            raise HTTPException(status_code=400, detail="Image file invalid")

        binMessage: str = ""
        for letter in messageText:
            binMessage += format(ord(letter), "08b")

        binImgData: str = ""
        for px in imgPixels:
            binImgData += bin(px[0])[-1] + bin(px[1])[-1] + bin(px[2])[-1]

        if is_image_already_encoded(binImgData, binMessage):
            raise HTTPException(
                status_code=400,
                detail="Image or message have already been encoded"
            )

        binMessage = XML_START + binMessage + XML_END

        if not is_img_long_enough(binMessage, imgWidth, imgHeight):
            raise HTTPException(
                status_code=400, detail="Image too small to contain message"
            )

        logger.info("Image meets requirements")

        requiredPixels = len(binMessage) // 3 + 1

        encodeLocation: int = get_encode_location(
            requiredPixels, len(imgPixels)
        )

        logger.info("Initiating pixel modification")

        imgPixels = encode_image(
            encodeLocation, requiredPixels, imgPixels, binMessage
        )

        img.putdata(imgPixels)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        object_key = f"{uuid4().hex}.png"

        img_filepath: str = save_img_local(
            filename=object_key,
            subdir="encoded",
            img_data=img_bytes
        )

        return img_filepath

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Something went wrong")
