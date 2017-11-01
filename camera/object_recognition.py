import numpy as np

from PIL import Image

from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
from keras.applications import imagenet_utils
from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import decode_predictions


print("[INFO] loading network...")
model = InceptionV3(include_top=True, weights='imagenet')
print("Model loaded.")


def classify_image(image):
    prediction = decode_predictions(model.predict(image))[0][0][1]
    return str(prediction)


def extract_image(image_file):
    image = Image.open(image_file)
    image = image.resize((299, 299), Image.ANTIALIAS)
    image = image_utils.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    image = image.astype(np.float64, casting='unsafe')

    return image

