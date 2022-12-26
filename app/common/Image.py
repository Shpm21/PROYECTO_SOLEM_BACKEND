from flask_restful import Resource, request

from app.logic.Detector import Detector
from app.logic.TransformImage import TransformImage

transform_image = TransformImage.getInstance()


class ImageEndPoint(Resource):
    def get(self):
        return {'image': 'image'}

    def post(self):
        images = []
        # get the image from the request, this image is in base64
        image = request.form['image']
        real_image = transform_image.get_encode_from_metadata(
            image)
        img = transform_image.get_and_save_image_grey_equalize_binarize(
            real_image)
        images = transform_image.get_images_to_show()
        transform_image.clear_images_to_show()
        letters = Detector.getInstance().detect(img)
        return {'letters': letters, 'images': images}
