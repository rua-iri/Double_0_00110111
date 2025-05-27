# Double_0_00110111

This is a Python API to carry out [Steganography](https://en.wikipedia.org/wiki/Steganography) on images.

<div align="center">
  <div>
    </div>
      <br>
    <img src="https://github.com/rua-iri/Double_0_00110111/assets/117874491/87f53b7e-528d-4304-a6ec-6513dc41e9f3" alt="logo" width="35%" />
  <br>
</div>

## Setup

```bash
git clone https://github.com/rua-iri/Double_0_00110111.git

cd Double_0_00110111

docker compose up --build
```

### Sanity Check

```bash
curl localhost:8000/helloworld
```

## Test

The tests will be run as part of the Docker compose process, however if you would like to run them again then use the following command.

```
docker exec <container_name> python3 -m test -v
```

## Demonstration

The application is designed to encode images in a manner that is imperceptable to the human eye.

| Input Image                                                                                                    | Output Image                                                                                                           |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ![image](https://raw.githubusercontent.com/rua-iri/Double_0_00110111/refs/heads/main/fastapi_backend/sample_images/sample.png) | ![image](https://raw.githubusercontent.com/rua-iri/Double_0_00110111/refs/heads/main/fastapi_backend/sample_images/sample_encoded.png) |

The image has been encoded by modifying the binary values of each single pixel in a small section of the image so that it can contain the message.

| Difference                                                                                |
| ----------------------------------------------------------------------------------------- |
| ![image](https://github.com/user-attachments/assets/df57e53d-75cd-42a8-a22c-547868a46261) |

As you can see there is a single red line at the top of the file where the message has been secretly embedded in the image.

If you would like to demonstrate how this works then run the following to output the difference between the original and encoded images.

```bash
compare -compose src <input_image.png> <output_image.png> image_diff.png
```
