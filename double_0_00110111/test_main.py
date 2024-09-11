from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_encode():
    response = client.post("/encode")
    pass


def test_decode():
    response = client.post("/decode")
    pass


def test_get_encoded_image():
    response = client.get("/image/{img_filename}")
    pass
