import cv2
import time
import os
import hand_tracking_module as htm
import pyautogui

cap=cv2.VideoCapture(0)



detector=htm.handDetector(detectionCon=0.75)
tipIds=[4,8,12,16,20]
while True:
    success,img=cap.read()
    img=detector.findHands(img)
   # cv2.imshow(img)
    lmList=detector.findPosition(img,draw=False)
    #print(lmList)
    if len(lmList) !=0:
        fingers=[]

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]: #
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):  #y axis
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers=fingers.count(1)
        if totalFingers == 5:
            pyautogui.press('space')
        elif totalFingers==1:
            pyautogui.press('up')
        elif totalFingers==2:
            pyautogui.press('down')
        elif totalFingers==3:
            pyautogui.press('right')
            time.sleep(0.5)
        elif totalFingers==4:
            pyautogui.press('left')
            time.sleep(0.5)

        # if totalFingers == 5:
        #     pyautogui.press('space')
        # elif totalFingers==1:
        #     pyautogui.press('left')
        #     time.sleep(1)
        # elif totalFingers==2:
        #     pyautogui.press('right')
        #     time.sleep(1)
        # elif totalFingers==3:
        #     pyautogui.press('down')
        # elif totalFingers==4:
        #     pyautogui.press('up')
        
         

        print(totalFingers)





    cv2.imshow("Image",img)
    cv2.waitKey(1)