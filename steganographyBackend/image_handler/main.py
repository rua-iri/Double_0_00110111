import json
import sys
import os
from PIL import Image
import random
import logging
import helpers
import io

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


# check if image is large enough to store message
def isImgLongEnough(msg: str, wdth: int, hght: int) -> bool:
    if (len(msg) // 3 + 1) < (wdth * hght):
        return True
    else:
        return False


# return a list of the binary representations of the xml tags
def getXmlTags() -> tuple:
    return (
        "".join(format(ord(c), "08b") for c in "<msg>"),
        "".join(format(ord(c), "08b") for c in "</msg>"),
    )


# get random location in the image to encode the message
def getEncodeLocation(reqPixels: int, maxPixels: int) -> int:
    encodeLocation = random.randint(0, (maxPixels - reqPixels))

    # regenerate encodeLocation until it is divisible by 8
    while encodeLocation % 8:
        encodeLocation = random.randint(0, (maxPixels - reqPixels))

    return encodeLocation


# function to encode message in a given image
def writeToImage(image_data, messageText):
    try:
        img = Image.frombytes(io.BytesIO(image_data))
        imgWidth, imgHeight = img.size
        imgPixels = list(img.getdata())

        binMessage = ""
        for letter in messageText:
            binMessage += format(ord(letter), "08b")

        # enclose the message in xml tags
        openTag, closeTag = getXmlTags()

        binaryData = ""
        for px in imgPixels:
            binaryData += bin(px[0])[-1] + bin(px[1])[-1] + bin(px[2])[-1]

        # check image and message are valid
        if openTag in binaryData or closeTag in binaryData: raise Exception("Invalid Message")
        if openTag in binMessage or closeTag in binMessage: raise Exception("Image written to previously")

        binMessage = openTag + binMessage + closeTag

        if not isImgLongEnough(binMessage, imgWidth, imgHeight): raise Exception("Image too small")

        requiredPixels = len(binMessage) // 3 + 1

        # generate random encode location
        encodeLocation = getEncodeLocation(requiredPixels, len(imgPixels))

        bIndex = 0
        # iterate through each pixel to be modified
        for i in range(encodeLocation, (encodeLocation + requiredPixels)):
            # convert to list so that values can be reassigned
            imgPixels[i] = list(imgPixels[i])

            # iterate through each colour value for each pixel
            for x in range(len(imgPixels[i])):

                # check if i < binMessage length
                if bIndex < len(binMessage):
                    imgPixels[i][x] = int(
                        bin(imgPixels[i][x])[:-1] + binMessage[bIndex], 2
                    )
                    bIndex += 1

            imgPixels[i] = tuple(imgPixels[i])

        # generate a new name for the file to be saved
        newFileName = imgName.replace("uploads", "downloads")
        newFileName = newFileName.split(".")[0] + ".png"

        # write to a new image (must be a png file for lossless compression)
        encodedImg = Image.new(img.mode, img.size)
        encodedImg.putdata(imgPixels)
        encodedImg.save(fp=newFileName, format="PNG")

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
        operation, message, image = helpers.parse_form_data(event=event)

        if operation == "encode":
            # TODO: load image from event
            # TODO: pass secret message and image stream to writeToImage() function
            pass
        elif operation == "decode":
            pass
        else:
            raise Exception

        # check that the right number of arguments has been passed
        # and call different function depending on the first argument
        if len(argv) == 3 and argv[0] == "encode":
            imgPath = argv[1]
            encodeString = argv[2]
            writeToImage(imgPath, encodeString)
        elif len(argv) == 2 and argv[0] == "decode":
            imgPath = argv[1]
            readFromImage(imgPath)
        else:
            print("0")

    except Exception as e:
        logger.error(e)
