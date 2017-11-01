from flask import Flask
from flask import request

from camera.object_recognition import classify_image
from camera.object_recognition import extract_image


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Testing Continuous Deployment'


@app.route('/object_recognition', methods=['POST'])
def object_recognition():
    image = extract_image(request.files['file'])
    prediction = classify_image(image)
    return prediction


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
