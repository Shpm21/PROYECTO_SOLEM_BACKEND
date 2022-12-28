from flask_restful import Resource, request

from app.logic.Detector import Detector
from app.logic.ImageValidator import ImageValidator
from app.logic.TransformImage import TransformImage

image_validator = ImageValidator.getInstance()
transform_image = TransformImage.getInstance()
detector = Detector.getInstance()


def transform_image_to_cv2(image):
    # transform image to opencv image
    return transform_image.transform_image_to_cv2(image)


def get_encode_from_metadata(image):
    # get the image in base64
    return image.split(',')[1]


def imageIsValid(image):
    # validate the image
    return image_validator.validate_image(image)


def decode_image(image):
    # decode the image
    return transform_image.decode_image(image)


class ImageEndPoint(Resource):
    def get(self):
        return {'image': 'image'}

    def post(self):
        images = []
        # get the image from the request, this image is in base64
        image = request.form['image']
        real_image = decode_image(
            get_encode_from_metadata(image))  # decode the image
        # transform image to opencv image
        image_test = transform_image_to_cv2(real_image)

        img = transform_image.get_and_save_image_grey_equalize_binarize(
            real_image)
        images = transform_image.get_images_to_show()  # get the images to show
        transform_image.clear_images_to_show()  # clear the images to show
        text = detector.detect(img)  # detect the text in the image

        image_validator.train()  # train the model to validate the image
        is_valid = imageIsValid(image_test)  # validate the image
        # return the text, the images and if the image is valid
        return {'text': text, 'images': images, 'isValid': is_valid}
