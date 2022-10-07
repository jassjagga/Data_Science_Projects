import joblib
import json
import numpy as np
import cv2
from wavelet import w2d


def classify_image(image_base64,file_path=None):
    pass

def get_cropped_image_if_2_eyes(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    if image_path:
        img=cv2.imread(image_path)
    else:
        img=get_cv2_image_form_base64_string(image_base64_data)

    if img is not None:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=img[y:y+h,x:x+w]
            eyes=eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) >=2:
                return roi_color

def get_b64_test_image_for_elli():
    with open("b64.txt") as f:
        return f.read()

if __name__ =="__main__":
    print(classify_image(get_b64_test_image_for_elli(),None))