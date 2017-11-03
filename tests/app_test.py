import mock

from app import object_recognition
from camera.object_recognition import extract_image


IMAGE = extract_image('tests/camera/dog.jpg')


@mock.patch('app.request')
@mock.patch('app.extract_image', return_value=IMAGE)
def test_object_recognition(mock_request, mock_extract_image):
    assert object_recognition() == 'beagle'
