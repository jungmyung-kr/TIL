# pip install mediapipe

"""
Basics
"""

############
# Module import
############

import cv2
import mediapipe as mp
import time  # to check the frame rate


##########################
# 웹캠 잘 작동하는 지 확인할 기본 코드
##########################

cap = cv2.VideoCapture(0)  # 0번째 카메라 장치

if not cap.isOpened():  # 카메라가 잘 열리지 않은 경우
    exit()  # 프로그램 종료

while True:  # 카메라가 열리면
    succeess, img = cap.read()

    cv2.imshow('Image', img)

    if cv2.waitKey(1) == ord('q'):
        # 카메라의 경우 동영상의 끝이 없기 때문에, 사용자가 직접 q를 입력해야 종료됨.
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


###################################
# 손의 21개 랜드마크 및 각 랜드마크 연결 여부 확인
###################################

cap = cv2.VideoCapture(0)  # 0번째 카메라 장치

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils  # with this it draws

'''
default parameters : 

static_image_mode = False
max_num_hands = 2
min_detection_confidence = 0.5
min_tracking_confidence = 0.5
'''

if not cap.isOpened():
    exit()

while True:
    succeess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # convert to RGB : Object "hands" only uses RGB
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    '''
    if it detects : 
    ex)
        landmark {
      x: 0.7253167629241943
      y: -0.035633206367492676
      z: -0.09244664013385773
    }

    if not : 

        None
    '''

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # could be one or more
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            # without mpHands.HAND_CONNECTIONS, it will just show 21 landmarks

    cv2.imshow('Image', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


############
# 화면에 fps 출력
############

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0  # previous time
cTime = 0  # current time

if not cap.isOpened():
    exit()

while True:
    succeess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    # (10, 70) : position / font / scale / color / thickness

    cv2.imshow('Image', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


###############################
# 인덱스와 랜드마크 얻기(각 포인트별 좌표값)
###############################

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

if not cap.isOpened():
    exit()

while True:
    succeess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # each id has corresponding landmark (x, y, z)
                # and We will use x, y to find the info or location of the hand

                # print(id, lm)
                '''
                0 x: 0.600256085395813
                y: 1.019203543663025
                z: 1.1256701526463075e-07

                id (0 ~ 20) 
                0 indicates wrist
                20 indicates pinky tip
                '''

                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # since the x, y values are decimal, we need to rescale it
                print(id, cx, cy)  # ex) 0 993 484

                # if we want to draw some figure on specific index,
                if id == 0:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    # draw circle on index 0 (center, radius, color)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow('Image', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)