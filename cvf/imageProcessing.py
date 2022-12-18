# -*- coding: utf-8 -*-
import pytesseract
import cv2
try:
    from PIL import Image
except ImportError:
    import Image


def processRequestImage(requestImage):
    img = Image.open(requestImage)
    print("Image size: ",img.size) 
    img = img.convert('L')  # greyscale
    # img.save('testingSaving.png') # guardando en el fileSystem la imagen recibida

    textDetected = pytesseract.image_to_string(img)
    print(textDetected)
    return textDetected


def processFileSystemImage():
    image_path = "./TestingTextDetection.png"
    image_path = "./TestingTextDetection.jpg"

    windowSize = (1000, 563)
    cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Result', windowSize[0], windowSize[1])

    # using 0 as second argument turns the image into grayscale
    img = cv2.imread(image_path, 0)
    # img = cv2.cvtColor(img, cv2.THRESH_OTSU)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_string(img))
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(imgGray, (5, 5), 1)

    # # DETECTING CHARACTERS
    hImg, wImg = img.shape
    boxes = pytesseract.image_to_boxes(img)
    print(pytesseract.image_to_string(img))
    for b in boxes.splitlines():
        posData = b.split(" ")
        x, y, w, h = int(posData[1]), int(
            posData[2]), int(posData[3]), int(posData[4])
        cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
        cv2.putText(img, posData[0], (x-40, hImg-y+20),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

    # DETECTING WORDS
    hImg, wImg = img.shape
    # TO ONLY DETECT DIGITS
    # cong = r'--oem 3 --psm 6 outputbase digits'
    # boxes = pytesseract.image_to_data(img, config=cong)

    # boxes = pytesseract.image_to_data(img, config="OEM_CUBE_ONLY TESSERACT")
    # boxesIter = boxes.splitlines()
    # for i in range(1, len(boxesIter)):
    #     boxDataArr = boxesIter[i].split()
    #     if len(boxDataArr) == 12:
    #         print(boxDataArr[-1])
    #         x, y, w, h = int(boxDataArr[6]), int(boxDataArr[7]), int(
    #             boxDataArr[8]), int(boxDataArr[9])
    #         cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)
    #         cv2.putText(img, boxDataArr[11], (x-20, y),
    #                     cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

    cv2.imshow('Result', img)
    cv2.waitKey(0)