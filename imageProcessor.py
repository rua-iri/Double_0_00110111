from PIL import Image


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
    binaryMessage = openTag + binaryMessage + closeTag

    # TODO use checkIsLongEnough function before the rest of stuff is executed


    # TODO check if file is in a lossless compression format
    # probably using the get_format_mimetype() method on the image
    # alternatively we could accept all filetypes but EXPORT as png only


    # TODO add xml markers to signify where the message begins and ends


    # TODO encode the message at a random location within the file


    # TODO forbid users from including <msg> or </msg> in their messages

    # TODO maybe add a second type of encryption for the message contents


    # determine the max number of pixels that must be modified to encode the message
    requiredPixels = len(binaryMessage) // 3 + 1

    bIndex = 0
    # iterate through each pixel to be modified
    for i in range(requiredPixels):

            # convert to list so that values can be reassigned
            imgPixels[i] = list(imgPixels[i])

            # iterate through each colour value for each pixel
            for x in range(len(imgPixels[i])):

                # check if i < binaryMessage length
                if bIndex < len(binaryMessage):
                    imgPixels[i][x] = int(bin(imgPixels[i][x])[:-1] + binaryMessage[bIndex], 2)
                    bIndex+=1
            
            imgPixels[i] = tuple(imgPixels[i])


    # write to a new image
    encodedImg = Image.new(img.mode, img.size)
    encodedImg.putdata(imgPixels)
    encodedImg.save("encoded_" + imgName)





def readFromImage(fileName):
    img = Image.open(fileName)
    imgPixels = list(img.getdata())

    # concatenate the data from the least significant bit of every pixel
    binaryData = ""


    for px in imgPixels:
        binaryData += bin(px[0])[-1] + bin(px[1])[-1] + bin(px[2])[-1]


    # TODO remove this
    print(binaryData.find("010010000110010101101100011011000110111100101100001000000101011101101111011100100110110001100100"))
    

    # find the start and the end using the binary values for the xml tags
    openTag, closeTag = getXmlTags()
    msgStart = binaryData.find(openTag) + len(openTag)
    msgEnd = binaryData.find(closeTag)

    # decode binary into readable text
    totalText= ""
    # for i in range(len(binaryData)//8):
    for i in range((msgStart//8), (msgEnd//8)):
        charStart = i*8
        charEnd = (i+1)*8
        totalText += chr(int(binaryData[charStart:charEnd], 2))

    # TODO remove this
    with open("Blah.txt", "w") as blahFile:
        blahFile.write(totalText)

    print(totalText)
    print(len(totalText))





# writeToImage("testImage.png", "This message is a test...")
readFromImage("encoded_testImage.png")



