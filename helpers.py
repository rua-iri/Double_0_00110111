
from constants import XML_START, XML_END
import random


# check if image is large enough to store message
def isImgLongEnough(msg: str, wdth: int, hght: int) -> bool:
    if (len(msg) // 3 + 1) < (wdth * hght):
        return True
    else:
        return False



def is_image_already_encoded(binary_img_data: str, binary_message: str) -> bool:
    # check image and message are valid
        if XML_START in binary_img_data or XML_END in binary_img_data: 
            raise Exception("Invalid Message")
        if XML_START in binary_message or XML_END in binary_message: 
            raise Exception("Image written to previously")
        
        return True



# get random location in the image to encode the message
def get_encode_location(reqPixels: int, maxPixels: int) -> int:
    encodeLocation = random.randint(0, (maxPixels - reqPixels))

    # regenerate encodeLocation until it is divisible by 8
    while encodeLocation % 8:
        encodeLocation = random.randint(0, (maxPixels - reqPixels))

    return encodeLocation



def save_encoded_image(img_name, img_data):
    img_location = f"encoded/{img_name}"
    try:
        with open(img_location, "wb") as img_file:
            img_file.write(img_data)

    except Exception as e:
        raise e
        


def encode_image(
        encode_location: int, 
        required_pixels: int, 
        image_pixels: list, 
        binary_message: str):

    binary_index = 0
    # iterate through each pixel to be modified
    for pixelIndex in range(encode_location, (encode_location + required_pixels)):
        # convert to list to make mutable
        image_pixels[pixelIndex] = list(image_pixels[pixelIndex])

        # iterate through each colour value for each pixel
        for colourIndex in range(len(image_pixels[pixelIndex])):
            if binary_index < len(binary_message):
                
                image_pixels[pixelIndex][colourIndex] = int(
                    bin(image_pixels[pixelIndex][colourIndex])[:-1] + binary_message[binary_index], 2
                )
                
                binary_index += 1

        # convert back to tuple
        image_pixels[pixelIndex] = tuple(image_pixels[pixelIndex])

    
    return image_pixels


    

