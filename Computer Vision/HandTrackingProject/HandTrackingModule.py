import cv2
import mediapipe as mp
import time


class handDetector():

    def __init__(self, mode=False, maxHands=2, complexity=1, detectionCon=0.5, trackCon=0.5):
        self.results = results
        self.mode = mode
        self.maxHands = maxHands
        self.complexity = complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complexity,
                                        self.detectionCon, self.trackCon, )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:  # it will draw when we ask it to draw
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)

        return img


def main():
    pTime = 0
    cTime = 0

    cap = cv2.VideoCapture(0)

    detector = handDetector()

    if not cap.isOpened():
        exit()

    while True:
        succeess, img = cap.read()
        img = detector.findHands(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow('Image', img)

        if cv2.waitKey(1) == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)


if __name__ == "__main__":
    main()


'''
에러 발생, 수정 필요
---------------------------------------------------------------------------
error Traceback (most recent call last)
Input In [4], 
in <cell line: 73>() 69 cv2.waitKey(1) 73 if __name__ == "__main__" : ---> 74 main()

Input In [4],
 in main() 
 50 while True: 
 51 succeess, img = cap.read() 
 ---> 
 52 img = detector.findHands(img)
  54 cTime = time.time() 
  55 fps = 1/(cTime - pTime)
 
Input In [4], in handDetector.findHands(self, img, draw) 
24 def findHands(self, img, draw = True) : 
---> 
25 imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
27 self.results = self.hands.process(imgRGB) 
30 if self.results.multi_hand_landmarks:

error: OpenCV(4.6.0) /Users/runner/work/opencv-python/opencv-python/opencv/modules/imgproc/src/color.cpp:182: 
error: (-215:Assertion failed) !_src.empty() in function 'cvtColor'
'''