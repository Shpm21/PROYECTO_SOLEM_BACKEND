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
from matplotlib import pyplot as plt


class ImageProcessor():
    # PASOS A COMPLETAR
    # 1. Capturar la imagen
    # 2. Transformar a gris.
    # 3. Ecualizar la imagen (Ecualización de histograma)
    # 4. Otzu.
    # --------------------------------
    # Procesar la imagen (acondicionar)
    # Agregar a la aplicación
    # Enviar información pasada...

    # singleton
    __instance = None

    def __init__(self):
        if Detector.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Detector.__instance = self
    
    @staticmethod
    def getInstance():
        if Detector.__instance == None:
            Detector()
        return Detector.__instance

    # PRUEBA
    @staticmethod
    def getTextFromSampleImage():
        # -*- coding: utf-8 -*-
        print("Running sample function")
        # image_path = "/home/emilio/Documents/Projects/OpticalStuff/SOLEM_REPOS/PROYECTO_SOLEM_BACKEND/imagesLibrary/ColorTestingTextDetection.jpg"
        image_path = "./imagesLibrary/ColorTestingTextDetection.jpg"
        img = cv2.imread(image_path, -1)
        print(img)
        return "eeeeepico"

    # ORIGINAL PRIMERA
    @staticmethod
    def getTextFromImageBytes(imageBytes):
        # La flag en el método imdecode especifica el cómo debe leerse la imagen. La flag puede tomar valores 1,0,-1 etc.
        # >  1 especifica cv2.IMREAD_COLOR : Lee la imagen en formato de color BGR y elimina el canal alfa. Es el valor por defecto de la bandera.
        # >  0 especifica cv2.IMREAD_GRAYSCALE : Lee la imagen en escala de grises.
        # > -1 especifica cv2.IMREAD_UNCHANGED : Lee la imagen sin cambios, preserva el canal alfa.
        # Usamos 0 para dejar la imagen en escala de grises
        decodedImgArr = cv2.imdecode(np.frombuffer(imageBytes, np.uint8), 0) # la otra flag posible es: cv2.IMREAD_GRAYSCALE
        # print('ImagenOpenCV:\n', decodedImgArr) # sólo para saber cómo va la imagen
        
        decodedImgArr = cv2.cvtColor(decodedImgArr, cv2.THRESH_OTSU) # Por algún motivo esto falla si la flag usada es -1 en lugar de 0
        # print(decodedImgArr)

        boxes = pytesseract.image_to_data(decodedImgArr, config="OEM_CUBE_ONLY TESSERACT")
        # Usamos esta funcion dado que pytesseract.image_to_data entrega más información de la que necesitamos
        textArrs = obtainTextArraysFromImgs(boxes.splitlines())
        print(textArrs)

        # DISPLAY DE LA IMAGEN SÓLO EN DEVELOPMENT
        windowSize = (1000, 563)
        cv2.namedWindow('Result Image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Result Image', windowSize[0], windowSize[1])
        cv2.imshow('Result Image', decodedImgArr)
        cv2.waitKey()

        return textArrs

    # VERSION QUE USA LA ECUALIZACIÓN
    @staticmethod
    def getTextFromImageBytesEcualized_v1(imageBytes):
        print("\n\n\n\n\nRunning ImageProcessor.getTextFromImageBytesEcualized_v1\n\n")
        img = cv2.imdecode(np.frombuffer(imageBytes, np.uint8), -1) # la otra flag posible es: cv2.IMREAD_GRAYSCALE
        img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
        img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
        hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
        cv2.imwrite('./imagesLibrary/resultin.jpg',hist_equalization_result)

        image_path = "./imagesLibrary/resultin.jpg"
        img_grayscale = cv2.imread(image_path, 0)
        img_grayscale = cv2.cvtColor(img_grayscale, cv2.THRESH_OTSU)

        boxes = pytesseract.image_to_data(img_grayscale, config="OEM_CUBE_ONLY TESSERACT")
        # Usamos esta funcion dado que pytesseract.image_to_data entrega más información de la que necesitamos
        textArrs = obtainTextArraysFromImgs(boxes.splitlines())
        print(textArrs)

        # DISPLAY DE LA IMAGEN SÓLO EN DEVELOPMENT
        windowSize = (1000, 563)
        cv2.namedWindow('Result Image Ecualized', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Result Image Ecualized', windowSize[0], windowSize[1])
        cv2.imshow('Result Image Ecualized', hist_equalization_result)
        # cv2.imshow('Result Image Ecualized', img_to_yuv)
        cv2.waitKey()

        return textArrs


    # VERSION ALTERNATIVA DE LA ECUALIZACION
    @staticmethod
    def getTextFromImageBytesEcualized_v2(imageBytes):
        print("\n\n\n\n\nRunning ImageProcessor.getTextFromImageBytesEcualized_v2\n\n")
        decodedImgArr = cv2.imdecode(np.frombuffer(imageBytes, np.uint8), 0) # la otra flag posible es: cv2.IMREAD_GRAYSCALE
        decodedImgArr = cv2.cvtColor(decodedImgArr, cv2.THRESH_OTSU) # Por algún motivo esto falla si la flag usada es -1 en lugar de 0
        decodedImgArr = cv2.equalizeHist(decodedImgArr)

        boxes = pytesseract.image_to_data(decodedImgArr, config="OEM_CUBE_ONLY TESSERACT")
        # Usamos esta funcion dado que pytesseract.image_to_data entrega más información de la que necesitamos
        textArrs = obtainTextArraysFromImgs(boxes.splitlines())
        print(textArrs)

        # DISPLAY DE LA IMAGEN SÓLO EN DEVELOPMENT
        windowSize = (1000, 563)
        cv2.namedWindow('Result Image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Result Image', windowSize[0], windowSize[1])
        cv2.imshow('Result Image', decodedImgArr)
        cv2.waitKey()

        return textArrs

    @staticmethod
    def showHistFromImgBytes(imageBytes):
        npImgArr = cv2.imdecode(np.frombuffer(imageBytes, np.uint8), 0) # la otra flag posible es: cv2.IMREAD_GRAYSCALE
        npImgArr = cv2.cvtColor(npImgArr, cv2.THRESH_OTSU) # Por algún motivo esto falla si la flag usada es -1 en lugar de 0

        # hist = cv2.calcHist([npImgArr],[0],None,[256],[0,256])
        # plt.hist(npImgArr.ravel(),256,[0,256])
        # plt.title('Result Image Histogram')
        # plt.show()
        # print("\n\n\nHistograma\n\n\n",hist)

        color = ('b','g','r')
        for channel,col in enumerate(color):
            histr = cv2.calcHist([npImgArr],[channel],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])
        plt.title('Histogram for color scale picture')
        plt.show()

        while True:
            k = cv2.waitKey(0) & 0xFF     
            if k == 27: break             # ESC key to exit 
        cv2.destroyAllWindows()
