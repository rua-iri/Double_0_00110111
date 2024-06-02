import json
from uuid import uuid4
from PIL import Image
import random
import logging
import io
import helpers
from constants import XML_START, XML_END

from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import FileResponse
from typing import Union, Annotated


app = FastAPI()



logger = logging.getLogger()
logger.setLevel(level=logging.INFO)




# check if image is large enough to store message
def isImgLongEnough(msg: str, wdth: int, hght: int) -> bool:
    if (len(msg) // 3 + 1) < (wdth * hght):
        return True
    else:
        return False


# get random location in the image to encode the message
def getEncodeLocation(reqPixels: int, maxPixels: int) -> int:
    encodeLocation = random.randint(0, (maxPixels - reqPixels))

    # regenerate encodeLocation until it is divisible by 8
    while encodeLocation % 8:
        encodeLocation = random.randint(0, (maxPixels - reqPixels))

    return encodeLocation


# function to encode message in a given image
def write_to_image(image_data: bytes, messageText: str) -> dict:
    try:
        img = Image.open(io.BytesIO(image_data))
        imgWidth, imgHeight = img.size
        imgPixels = list(img.getdata())

        if img.format != "PNG":
            raise Exception("Image must be png format")

        binMessage = ""
        for letter in messageText:
            binMessage += format(ord(letter), "08b")

        binImgData = ""
        for px in imgPixels:
            binImgData += bin(px[0])[-1] + bin(px[1])[-1] + bin(px[2])[-1]

        # check image and message are valid
        if XML_START in binImgData or XML_END in binImgData: 
            raise Exception("Invalid Message")
        if XML_START in binMessage or XML_END in binMessage: 
            raise Exception("Image written to previously")

        binMessage = XML_START + binMessage + XML_END

        if not isImgLongEnough(binMessage, imgWidth, imgHeight): 
            raise Exception("Image too small")

        logger.info("Image meets requirements")

        requiredPixels = len(binMessage) // 3 + 1

        encodeLocation = getEncodeLocation(requiredPixels, len(imgPixels))

        logger.info("Initiating pixel modification")
        binaryIndex = 0
        # iterate through each pixel to be modified
        for pixelIndex in range(encodeLocation, (encodeLocation + requiredPixels)):
            # convert to list to make mutable
            imgPixels[pixelIndex] = list(imgPixels[pixelIndex])

            # iterate through each colour value for each pixel
            for colourIndex in range(len(imgPixels[pixelIndex])):
                if binaryIndex < len(binMessage):
                    
                    imgPixels[pixelIndex][colourIndex] = int(
                        bin(imgPixels[pixelIndex][colourIndex])[:-1] + binMessage[binaryIndex], 2
                    )
                    
                    binaryIndex += 1

            # convert back to tuple
            imgPixels[pixelIndex] = tuple(imgPixels[pixelIndex])

        img.putdata(imgPixels)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        object_key = f"{uuid4().hex}.png"

        helpers.save_encoded_image(object_key, img_bytes)
        

        return {'status': 'success', 'url': f"/image/{object_key}"}

    except Exception as e:
        logger.error(e)
        raise e


# function to extract secret message from a file
def readFromImage(fileName):
    img = Image.open(fileName)
    imgPixels = list(img.getdata())

    # concatenate the data from the least significant bit of every pixel
    binaryData = ""
    for px in imgPixels:
        binaryData += bin(px[0])[-1] + bin(px[1])[-1] + bin(px[2])[-1]

    # find the start and the end using the binary values for the xml tags
    openTag, closeTag = getXmlTags()
    msgStart = binaryData.find(openTag) + len(openTag)
    msgEnd = binaryData.find(closeTag)

    if msgEnd != -1:

        # decode binary into readable text
        totalText = ""
        for i in range((msgStart // 8), (msgEnd // 8)):
            charStart = i * 8
            charEnd = (i + 1) * 8
            totalText += chr(int(binaryData[charStart:charEnd], 2))

        stemFileName = fileName.split("/")[-1]
        stemFileName = str(stemFileName.split(".")[0])
        newFileName = "downloads/decode/" + str(stemFileName) + ".txt"

        with open(newFileName, "w") as msgFile:
            msgFile.write(totalText)

    else:
        print("0")


def lambda_handler(event, context):
    """
    Main function to handle event passed by api call
    """
    try:
        logger.info(f"Event: {event}")
        logger.info("Parsing event body")
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*'
        }
        
        operation, message, image = helpers.parse_form_data(event=event)

        if operation == "encode":
            body = write_to_image(image['value'], message)
        elif operation == "decode":
            body = {}
        else:
            raise Exception("Operation Not Specified")

        
        return {
            "headers": headers,
            "statusCode": 200,
            "body": json.dumps(body)
        }


    except Exception as e:
        logger.error(e)
        return {
            "headers": headers,
            "statusCode": 500,
            "body": json.dumps({"message": "Internal Server Error"})
        }





@app.get("/helloworld")
async def hello_world():
    """
    Hello World Endpoint for testing purposes
    """
    return {"Hello": "World"}




@app.post("/encode")
async def encode_image(
    message: Annotated[str, Form()], 
    file: UploadFile,
    ):

    image_data = await file.read()

    image_response = write_to_image(image_data=image_data, messageText=message)


    
    return {
        "Image Process": "Encode",
        "status": image_response.get("status"),
        "url": image_response.get("url"),
        }





@app.get("/image/{img_filename}")
async def get_encoded_image(img_filename: str):
    """
    Retrieve the encoded image for the user using the 
    """

    return FileResponse(f"encoded/{img_filename}")








        



