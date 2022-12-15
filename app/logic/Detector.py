import pytesseract


class Detector:
    # singleton
    __instance = None

    @staticmethod
    def getInstance():
        if Detector.__instance == None:
            Detector()
        return Detector.__instance

    def __init__(self):
        if Detector.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Detector.__instance = self

    def detect(self, image):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # detect the letters in the image using pytesseract
        letters = pytesseract.image_to_string(image)
        # return the letters
        return letters
