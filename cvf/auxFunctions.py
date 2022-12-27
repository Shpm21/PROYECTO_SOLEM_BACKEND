def obtainTextArraysFromImgs(boxesIter):
    obtainedWords = []
    for i in range(1, len(boxesIter)):
        boxDataArr = boxesIter[i].split()
        if len(boxDataArr) == 12:
            obtainedWords.append(boxDataArr[-1])
			# x, y, w, h = int(boxDataArr[6]), int(boxDataArr[7]), int(boxDataArr[8]), int(boxDataArr[9])
			# cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)
			# cv2.putText(img, boxDataArr[11], (x-20, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
    return obtainedWords

