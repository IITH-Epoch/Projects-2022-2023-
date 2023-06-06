import cv2
import mediapipe as mp
import time
import math
from subprocess import call
import pyautogui
import numpy as np

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

class handDetector():

    def __init__(self,mode=False,maxHands=2,modelComplexity=1,detectionConfidence=0.5,trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComplexity,self.detectionConfidence,self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils


    
    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks: # detecting all the hands
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS) #showing connections between points on hand

        return img
                

    def findPosition(self,img, handNo=0,draw=True):

        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w,),int(lm.y*h)
                # print(id ,cx, cy)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),14,(255,0,255),cv2.FILLED) #detecting a particular point of the 21 points detected by mediapipe

        return lmList
    
    def findDistance(self,img,x,y):
        lmList = self.findPosition(img,draw=False)
        if len(lmList) != 0:
            x1,y1 = lmList[x][1],lmList[x][2]
            x2,y2 = lmList[y][1],lmList[y][2]
            length = math.hypot(x1-x2,y1-y2)
            return length
        return 0
    
    def isFingerUp(self,img):
        lmList = self.findPosition(img,draw=False)
        returnList = [0,0,0,0,0]
        if len(lmList) != 0:
            if lmList[8][2] < lmList[6][2]:
                returnList[0] = 1

            if lmList[12][2] < lmList[10][2]:
                returnList[1] = 1

            if lmList[16][2] < lmList[14][2]:
                returnList[2] = 1

            if lmList[20][2] < lmList[18][2]:
                returnList[3] = 1

            if lmList[4][1] < lmList[2][1]:
                returnList[4] = 1
        return returnList         

                

def main():

    cLocX,cLocY = 0,0
    pLocX,pLocY = 0,0

    newTime = 0
    newTime4 = 0
    Ptime = 0
    Ctime = 0

    wCam, hCam = 640,480
    frameR = 70

    cap = cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)
    
    detector = handDetector(detectionConfidence=0.75,trackConfidence=0.75)

    while True:
        success, img = cap.read()

        img = detector.findHands(img,draw=True)

        returnList = detector.isFingerUp(img)
        # print(returnList)

        # gesture controlled volume control

        if(returnList[1] == 0 and returnList[2] == 0 and returnList[3]):
            length = detector.findDistance(img,4,8)
            if length >= 150:
                volume.SetMasterVolumeLevel(0,None)
            elif length <= 10:
                volume.SetMasterVolumeLevel(-65,None)
            else:
                newVolume = 0.464*(length-150)
                volume.SetMasterVolumeLevel(newVolume,None)
            # print(volume.GetMasterVolumeRange())

        # mouse move simulation using index finger

        if(returnList[0] and returnList[1] == 0 and returnList[2] == 0 and returnList[3] == 0):
            lmList = detector.findPosition(img,draw=False)
            x1,y1 = lmList[8][1],lmList[8][2]
            width, height = pyautogui.size()

            cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
            cv2.rectangle(img,(frameR-10,10),(wCam-frameR,hCam-frameR),(255,50,255),3)

            x3 = np.interp(x1,(frameR,wCam-frameR),(0,width))
            y3 = np.interp(y1,(frameR,hCam-frameR),(0,height))

            cLocX = pLocX + (x3-pLocX)/4
            cLocY = pLocY + (y3-pLocY)/4

            pyautogui.FAILSAFE = False
            pyautogui.moveTo(width-cLocX,cLocY,duration=0.1,_pause=False)

            pLocX,pLocY = cLocX,cLocY
        
        # single mouse click simluation two fingers

        if(returnList[0] and returnList[1] and returnList[2] == 0 and returnList[3] == 0):
            newTime2 = time.time()
            if abs(newTime2 - newTime) > 0.5:
                pyautogui.leftClick(_pause=True)
                newTime = time.time()
        
        # double mouse click simulation three fingers

        if(returnList[0] and returnList[1] and returnList[2] and returnList[3] == 0):
            newTime3 = time.time()
            if abs(newTime3 - newTime4) > 0.5:
                pyautogui.doubleClick(_pause=True)
                newTime4 = time.time()

        # screen scroll down using four fingers

        if(returnList[0] and returnList[1] and returnList[2] and returnList[3] and returnList[4] == 0):
            pyautogui.PAUSE = 0
            for s in range(20):
                pyautogui.scroll(-5)

        # screen scroll up using five fingers

        if(returnList[0] and returnList[1] and returnList[2] and returnList[3] and returnList[4]):
            pyautogui.PAUSE = 0
            for s in range(20):
                pyautogui.scroll(5)

        # to calculate fps
        Ctime = time.time()
        fps = 1/(Ctime-Ptime)
        Ptime = Ctime

        # to print fps
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,255),3)

        cv2.imshow("Image",img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()