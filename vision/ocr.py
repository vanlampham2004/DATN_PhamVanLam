import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"E:\DATN_Appnium\tesseract.exe"

def extract_text(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise Exception("Không đọc được ảnh")

    #  resize nhỏ lại
    img = cv2.resize(img, None, fx=0.5, fy=0.5)

    text = pytesseract.image_to_string(img)
    return text
