from time import time

import cv2

def compare_and_highlight(img1_path, img2_path, output="reports/diff_{timestamp}.png"):

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

    diff = cv2.absdiff(img1, img2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result = img2.copy()
    errors = 0

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w * h > 500:
            cv2.rectangle(result, (x,y), (x+w,y+h), (0,0,255), 2)
            errors += 1

    cv2.imwrite(output, result)
    return errors, output