import base64
import cv2
import base64


def get_base64_image(path: str):
    img = cv2.imread(path)
    _, im_arr = cv2.imencode('.jpg', img)
    img_base64 = base64.b64encode(im_arr).decode('utf-8')
    return img_base64


class TransformImage:
    __instance = None
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

    def get_encode_from_metadata(self, metadata):
        return metadata.split(',')[1]

    def get_and_save_image_rgb(self, image):
        image_64_decode = base64.b64decode(image)
        image_result = open('deer_decode.jpg', 'wb')
        image_result.write(image_64_decode)
        img = cv2.imread('./deer_decode.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite('deer_decode.jpg', img)
        self.append_image_to_show(
            get_base64_image('deer_decode.jpg'),
            'RGB'
        )
        return cv2.imread('deer_decode.jpg')

    def get_and_save_image_grey(self, image):
        img = self.get_and_save_image_rgb(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return self.save_and_return_image(
            img,
            'deer_decode_grey.jpg',
            'Grey'
        )

    def get_and_save_image_grey_equalize(self, image):
        img = self.get_and_save_image_grey(image)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        img = clahe.apply(img)
        return self.save_and_return_image(
            img,
            'deer_decode_grey_equalize.jpg',
            'Grey equalize'
        )

    def get_and_save_image_grey_equalize_binarize(self, image):
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
        self.images_to_show.append({
            'image': image,
            'description': description,
        })

    def save_and_return_image(self, image, path, description):
        cv2.imwrite(path, image)
        self.append_image_to_show(
            get_base64_image(path),
            description
        )
        return cv2.imread(path, 0)

    def clear_images_to_show(self):
        self.images_to_show = []
