from PIL import Image


# function to check if image is large enough to store message
def checkIsLongEnough(msg, wdth, hght):
    if (len(msg) // 3 + 1) < (wdth * hght):
        return True
    else:
        return False

def writeToImage(imgName, textToEncode):

    img = Image.open(imgName)
    imgWidth, imgHeight = img.size
    imgPixels = list(img.getdata())

    binaryMessage = ""

    for ltr in textToEncode:
        binaryMessage += format(ord(ltr), "08b")

    

    # TODO use checkIsLongEnough function before the rest of stuff is executed


    # TODO check if file is in a lossless compression format


    # TODO add xml markers to signify where the message begins and ends


    # TODO encode the message at a random location within the file


    # TODO remove this
    print(imgPixels[:33])
    for i in range(len(imgPixels[:33])):
        with open("imgInFile.txt", "a") as imgFile:
            imgFile.write(str(imgPixels[i]) + "\n")


    requiredPixels = len(binaryMessage) // 3 + 1

    bIndex = 0
    # iterate through each bit in the binary message
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



    # TODO remove this
    print(imgPixels[:33])
    for i in range(len(imgPixels[:33])):
        with open("imgOutFile.txt", "a") as imgFile:
            imgFile.write(str(imgPixels[i]) + "\n")

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
    for i in range(len(imgPixels[:33])):
        with open("imgDecodeFile.txt", "a") as imgFile:
            imgFile.write(str(imgPixels[i]) + "\n")

    # TODO remove this
    print(binaryData.find("010010000110010101101100011011000110111100101100001000000101011101101111011100100110110001100100"))
    


    # # decode binary into readable text
    # msgText= ""
    # for i in range(len(binaryData)//8):
    #     charStart = i*8
    #     charEnd = (i+1)*8
    #     msgText += chr(int(binaryData[charStart:charEnd], 2))

    # # TODO remove this
    # with open("Blah.txt", "w") as blahFile:
    #     blahFile.write(msgText[:30])

    # print(msgText[:20])
    # print(len(msgText))






writeToImage("testImage.png", "Hello, World")
readFromImage("encoded_testImage.png")




