import sys
from PIL import Image
import random

def main(argv):

    # check that the right number of arguments has been passed
    # and call different function depending on the first argument
    if len(argv)==3 and argv[0]=="encode":

        imgPath = argv[1]
        encodeString = argv[2]

        writeToImage(imgPath, encodeString)

    elif len(argv)==2 and argv[0]=="decode":
        imgPath = argv[1]

        readFromImage(imgPath)


    # TODO return error message if arguments are wrong
    else:
        pass


# function to check if image is large enough to store message
def checkIsLongEnough(msg, wdth, hght):
    if (len(msg) // 3 + 1) < (wdth * hght):
        return True
    else:
        return False


# function to return a list of the binary representations of the xml tags in which messages are enclosed
def getXmlTags():
    xTags = []
    xTags.append(''.join(format(ord(c), '08b') for c in "<msg>"))
    xTags.append(''.join(format(ord(c), '08b') for c in "</msg>"))
    return xTags


# function to get a random location in the image to encode the message
def getEncodeLocation(reqPixels, maxPixels):
    encodeLocation = random.randint(0, (maxPixels-reqPixels))

    # regenerate encodeLocation until it is divisible by 8
    while encodeLocation%8:
        encodeLocation = random.randint(0, (maxPixels-reqPixels))

    return encodeLocation



# function to encode message in a given image
def writeToImage(imgName, textToEncode):

    img = Image.open(imgName)
    imgWidth, imgHeight = img.size
    imgPixels = list(img.getdata())

    binaryMessage = ""

    for ltr in textToEncode:
        binaryMessage += format(ord(ltr), "08b")


    # enclose the message in the binary respresentation of the xml tags that 
    # signify the start and end of the message
    openTag, closeTag = getXmlTags()

    # check that binary message does not include xml tags before they are added
    isValidMessage = False if openTag in binaryMessage or closeTag in binaryMessage else True

    binaryMessage = openTag + binaryMessage + closeTag

    isMessageLongEnough = checkIsLongEnough(binaryMessage, imgWidth, imgHeight)

    # TODO maybe add a second type of encryption for the message contents

    # use checkIsLongEnough to ensure that image has enough pixels
    if isValidMessage and isMessageLongEnough:

        # determine the max number of pixels that must be modified to encode the message
        requiredPixels = len(binaryMessage) // 3 + 1

        # generate random encode location
        encodeLocation = getEncodeLocation(requiredPixels, len(imgPixels))
        

        bIndex = 0
        # iterate through each pixel to be modified
        for i in range(encodeLocation, (encodeLocation+requiredPixels)):

                # convert to list so that values can be reassigned
                imgPixels[i] = list(imgPixels[i])

                # iterate through each colour value for each pixel
                for x in range(len(imgPixels[i])):

                    # check if i < binaryMessage length
                    if bIndex < len(binaryMessage):
                        imgPixels[i][x] = int(bin(imgPixels[i][x])[:-1] + binaryMessage[bIndex], 2)
                        bIndex+=1
                
                imgPixels[i] = tuple(imgPixels[i])


        # generate a new name for the file to be saved
        stemFileName = imgName.split("/")[-1]
        stemFileName = str(stemFileName.split(".")[0])
        newFileName = "./downloads/" + stemFileName + "_encoded" +  ".png"

        # write to a new image (must be a png file for lossless compression)
        encodedImg = Image.new(img.mode, img.size)
        encodedImg.putdata(imgPixels)
        encodedImg.save(fp=newFileName, format="PNG")

        # TODO delete original image after new image has been uploaded
        print(newFileName)

    # TODO return error message if the conditions have not been met
    else:
        return False




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

    if msgEnd!=-1:

        # decode binary into readable text
        totalText= ""
        for i in range((msgStart//8), (msgEnd//8)):
            charStart = i*8
            charEnd = (i+1)*8
            totalText += chr(int(binaryData[charStart:charEnd], 2))


        stemFileName = fileName.split("/")[-1]
        stemFileName = str(stemFileName.split(".")[0])
        newFileName = "downloads/messages/" + str(stemFileName)  + ".txt"

        with open(newFileName, "w") as msgFile:
            msgFile.write(totalText)

        print(newFileName)

    
    # TODO return error message indicating that no message was encoded in the image
    else:
        return False



if __name__=="__main__":
    main(sys.argv[1:])

