


def save_encoded_image(img_name, img_data):
    img_location = f"encoded/{img_name}"
    try:
        with open(img_location, "wb") as img_file:
            img_file.write(img_data)

    except Exception as e:
        raise e
        


    
