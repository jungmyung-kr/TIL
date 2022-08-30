# pip install mediapipe

import cv2
import mediapipe as mp
import time  # to check the frame rate

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    succeess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    cv2.imshow("Image", img)
    cv2.waitKey(1)