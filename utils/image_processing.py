import cv2
import os

def preprocess_image(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoise = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

    thresh = cv2.adaptiveThreshold(
        denoise, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    out_path = path.replace('.', '_clean.')
    cv2.imwrite(out_path, thresh)

    return out_path
