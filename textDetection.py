def testing123():
    # -*- coding: utf-8 -*-
    print("1234567890")
    import pytesseract
    import cv2
    try:
        from PIL import Image
    except ImportError:
        import Image

    image_path = "targetDoc.jpg"
    image_path = "TestingTextDetection.png"
    image_path = "TestingTextDetection.jpg"

    img = cv2.imread(image_path)
    text_detected = []
    boxes = pytesseract.image_to_data(img, config="OEM_CUBE_ONLY TESSERACT")
    boxesIter = boxes.splitlines()
    for i in range(1, len(boxesIter)):
        boxDataArr = boxesIter[i].split()
        if len(boxDataArr) == 12:
            text_detected.append(boxDataArr[-1])
    print(text_detected)
