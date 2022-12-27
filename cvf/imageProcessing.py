# -*- coding: utf-8 -*-
import base64
import random
import os
import shutil
import pytesseract
import cv2
import numpy as np
import io
from PIL import Image
from auxFunctions import obtainTextArraysFromImgs

def getTextFromSampleImage():
    # -*- coding: utf-8 -*-
    print("Running sample function")


def getTextFromImageBytes(imageBytes):
    # La flag en el método imdecode especifica el cómo debe leerse la imagen. La flag puede tomar valores 1,0,-1 etc.
    # >  1 especifica cv2.IMREAD_COLOR : Lee la imagen en formato de color BGR y elimina el canal alfa. Es el valor por defecto de la bandera.
    # >  0 especifica cv2.IMREAD_GRAYSCALE : Lee la imagen en escala de grises.
    # > -1 especifica cv2.IMREAD_UNCHANGED : Lee la imagen sin cambios, preserva el canal alfa.
    # Usamos 0 para dejar la imagen en escala de grises
    decodedImgArr = cv2.imdecode(np.frombuffer(imageBytes, np.uint8), 0)
    # print('OpenCV:\n', decodedImgArr) # sólo para saber cómo va la imagen
    boxes = pytesseract.image_to_data(decodedImgArr, config="OEM_CUBE_ONLY TESSERACT")
    # Usamos esta funcion dado que pytesseract.image_to_data entrega más información de la que necesitamos
    return obtainTextArraysFromImgs(boxes.splitlines())

def getTextFromImageBytes2(image):
    # print("1111111111111111111",type(image))
    image_64_decode = base64.b64decode(image)
    # print("1111111111111111111",image_64_decode)
    print("2222222222222222222",type(image_64_decode))
    # using 0 as second argument turns the image into grayscale
    # img = cv2.imread(image, 0)
    # print("222222222222222222", img)
    # img = cv2.cvtColor(img, cv2.THRESH_OTSU)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # imgTextContent = pytesseract.image_to_string(img)
    
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(imgGray, (5, 5), 1)

    # # DETECTING CHARACTERS
    # hImg, wImg = img.shape
    # boxes = pytesseract.image_to_boxes(img)
    # print(pytesseract.image_to_string(img))
    # for b in boxes.splitlines():
    #     posData = b.split(" ")
    #     x, y, w, h = int(posData[1]), int(
    #         posData[2]), int(posData[3]), int(posData[4])
    #     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
    #     cv2.putText(img, posData[0], (x-40, hImg-y+20),
    #                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

    # DETECTING WORDS
    # hImg, wImg = img.shape
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

    # cv2.imshow('Result', img)
    # cv2.waitKey(0)
    # print(boxes)
    # valores = [element for element in imgTextContent.split("\n") if ((element != " ") or (element != "\f") or (element != ""))]
    # print(valores)
    return ["hello 123"]


""" 

def mainProcess():
	image_path = "targetDoc.jpg"
	image_path = "TestingTextDetection.png"
	image_path = "TestingTextDetection.jpg"

	windowSize = (1000, 563)
	cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('Result', windowSize[0], windowSize[1])

	img = cv2.imread(image_path)
	# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	# print(pytesseract.image_to_string(img))

	# # DETECTING CHARACTERS
	hImg, wImg, _ = img.shape
	# boxes = pytesseract.image_to_boxes(img)
	# print(pytesseract.image_to_string(img))
	# for b in boxes.splitlines():
	#     posData = b.split(" ")
	#     x, y, w, h = int(posData[1]), int(
	#         posData[2]), int(posData[3]), int(posData[4])
	#     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
	#     cv2.putText(img, posData[0], (x-40, hImg-y+20),
	#                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

	# DETECTING WORDS
	hImg, wImg, _ = img.shape
	# TO ONLY DETECT DIGITS
	# cong = r'--oem 3 --psm 6 outputbase digits'
	# boxes = pytesseract.image_to_data(img, config=cong)

	boxes = pytesseract.image_to_data(img, config="OEM_CUBE_ONLY TESSERACT")
	boxesIter = boxes.splitlines()
	for i in range(1, len(boxesIter)):
		boxDataArr = boxesIter[i].split()
		if len(boxDataArr) == 12:
			print(boxDataArr[-1])
			x, y, w, h = int(boxDataArr[6]), int(boxDataArr[7]), int(
				boxDataArr[8]), int(boxDataArr[9])
			cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)
			cv2.putText(img, boxDataArr[11], (x-20, y),
						cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)


	cv2.imshow('Result', img)
	cv2.waitKey(0) 

"""

def RESPALDOgetTextFromReqImage(image):
    print(image)
    image_path = "./TestingTextDetection.png"
    image_path = "./TestingTextDetection.jpg"

    # windowSize = (1000, 563)
    # cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Result', windowSize[0], windowSize[1])

    # using 0 as second argument turns the image into grayscale
    img = cv2.imread(image_path, 0)
    img = cv2.cvtColor(img, cv2.THRESH_OTSU)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgTextContent = pytesseract.image_to_string(img)
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(imgGray, (5, 5), 1)

    # # DETECTING CHARACTERS
    # hImg, wImg = img.shape
    # boxes = pytesseract.image_to_boxes(img)
    # print(pytesseract.image_to_string(img))
    # for b in boxes.splitlines():
    #     posData = b.split(" ")
    #     x, y, w, h = int(posData[1]), int(
    #         posData[2]), int(posData[3]), int(posData[4])
    #     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
    #     cv2.putText(img, posData[0], (x-40, hImg-y+20),
    #                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

    # DETECTING WORDS
    # hImg, wImg = img.shape
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

    # cv2.imshow('Result', img)
    # cv2.waitKey(0)
    # print(boxes)
    valores = [element for element in imgTextContent.split("\n") if ((element != " ") or (element != "\f") or (element != ""))]
    print(valores)
    return ["hello 123"]