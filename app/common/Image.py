from flask_restful import Resource, request
import base64
from app.logic.Detector import Detector
images = []


def get_encode_from_metadata(metadata):
    return metadata.split(',')[1]


def save_image_to_disk(image):
    image_64_decode = base64.b64decode(image)
    # create a writable image and write the decoding result
    image_result = open('deer_decode.jpg', 'wb')
    image_result.write(image_64_decode)
    return image_64_decode


class Image(Resource):
    def get(self):
        return {'image': 'image'}

    def post(self):
        # the image is in base 64 format
        image = request.form['image']  # get the image from the request
        real_image = get_encode_from_metadata(image)  # remove the metadata
        image_64_decode = save_image_to_disk(
            real_image)  # save the image to disk
        # aca debe ir el llamado al algoritmo que detecta letras en la imagen
        letters = Detector.getInstance().detect('./deer_decode.jpg')
        images.append(image)  # append the image to the list
        # return the letters
        return {'letters': letters}
