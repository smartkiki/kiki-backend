from camera.object_recognition import classify_image
from camera.object_recognition import extract_image


def test_classify_image():
    IMAGE_URL = './tests/camera/dog.jpg'
    image = extract_image(open(IMAGE_URL, 'rb'))
    assert classify_image(image) == 'beagle'
