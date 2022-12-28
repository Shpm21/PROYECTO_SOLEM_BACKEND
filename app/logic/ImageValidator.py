import cv2
import pickle


class ImageValidator:
    # singleton
    __instance = None
    img_train = cv2.imread('./files/carnet_example.jpg', cv2.IMREAD_GRAYSCALE)

    @staticmethod
    def getInstance():
        if ImageValidator.__instance is None:
            ImageValidator()
        return ImageValidator.__instance

    def __init__(self):
        if ImageValidator.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ImageValidator.__instance = self

    def train(self):
        sift = cv2.SIFT_create()
        _, des1 = sift.detectAndCompute(self.img_train, None)
        dic = {
            'front': des1
        }
        with open('./app/db/database.pk1', 'wb') as f:
            pickle.dump(dic, f)

    def validate_image(self, image):
        with open('./app/db/database.pk1', 'rb') as f:
            b = pickle.load(f)
        desc_front = b['front']

        # paso la imagen de opencv a gris
        img_test = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sift = cv2.SIFT_create()
        _, des2 = sift.detectAndCompute(img_test, None)
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(desc_front, des2, k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.5 * n.distance:
                good.append([m])

        return len(good) > 20
