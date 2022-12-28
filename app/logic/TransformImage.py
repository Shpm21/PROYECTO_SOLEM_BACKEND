import base64

import cv2
import numpy as np


def get_base64_image(path: str):
    img = cv2.imread(path)
    _, im_arr = cv2.imencode('.jpg', img)
    img_base64 = base64.b64encode(im_arr).decode('utf-8')
    return img_base64


class TransformImage:
    __instance = None
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    images_to_show = []  # the format is \
    # [{'image': image,
    #  'description': text },
    # {'image_g': image_grey
    # 'description': text},
    # {'image_ge': image_grey_equalize
    # 'description': text},
    # {'image_geb': image_grey_equalize_binarize
    # 'description': text}]

    @staticmethod
    def getInstance():
        if TransformImage.__instance == None:
            TransformImage()
        return TransformImage.__instance

    def __init__(self):
        if TransformImage.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TransformImage.__instance = self

    def get_and_save_image_rgb(self, image):
        """Get the image in RGB format and save it"""
        img = self.transform_image_to_cv2(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return self.save_and_return_image(
            img,
            'deer_decode.jpg',
            'RGB'
        )

    def get_and_save_image_grey(self, image):
        """Get the image in grey format and save it"""
        img = self.get_and_save_image_rgb(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return self.save_and_return_image(
            img,
            'deer_decode_grey.jpg',
            'Grey'
        )

    def get_and_save_image_grey_equalize(self, image):
        """Get the image in grey equalize format and save it"""
        img = self.get_and_save_image_grey(image)
        img = self.clahe.apply(img)
        return self.save_and_return_image(
            img,
            'deer_decode_grey_equalize.jpg',
            'Grey equalize'
        )

    def get_and_save_image_grey_equalize_binarize(self, image):
        """Get the image in grey equalize binarize format and save it"""
        img = self.get_and_save_image_grey_equalize(image)
        _, img = cv2.threshold(
            img, 127, 255, cv2.THRESH_BINARY)
        return self.save_and_return_image(
            img,
            'deer_decode_grey_equalize_binarize.jpg',
            'Grey equalize binarize'
        )

    def get_images_to_show(self):
        return self.images_to_show

    def append_image_to_show(self, image: str, description: str):
        """Append the image to show in the view"""
        self.images_to_show.append({
            'image': image,
            'description': description,
        })

    def save_and_return_image(self, image, path, description):
        """Save the image and return it"""
        cv2.imwrite(path, image)
        self.append_image_to_show(
            get_base64_image(path),
            description
        )
        return image

    def clear_images_to_show(self):
        """Clear the images to show"""
        self.images_to_show = []

    def transform_image_to_cv2(self, image):
        """Transform the image to cv2 format"""
        npimg = np.fromstring(image, np.uint8)
        return cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    def get_encode_from_metadata(self, metadata):
        """Get the encode from the metadata"""
        return metadata.split(',')[1]

    def decode_image(self, image):
        """Decode the image"""
        return base64.b64decode(image)
