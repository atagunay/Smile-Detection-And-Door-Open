import numpy as np
import cv2
import time
import RPi.GPIO as GPIO
from threading import Thread


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

detect = False

def capture():
    global detect
    print("girdi")
    for x in range(20):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]

            smile = smileCascade.detectMultiScale(
                roi_gray,
                scaleFactor= 1.5,
                minNeighbors=15,
                minSize=(25, 25),
                )

            for i in smile:
                if len(smile)>1:
                    print("guldu")
                    detect = True
                    break
       
    print("cıktı")
     

def control():
    print("control girdi")
    global detect
    if detect == True:
        servoPin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPin, GPIO.OUT)
        pwm = GPIO.PWM(servoPin, 50)
        pwm.start(0)
        print("kontrol - girdi")
        pwm.ChangeDutyCycle(5)
        time.sleep(1)
        pwm.ChangeDutyCycle(10)
        time.sleep(1)
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
        print("kontrol çıktı")
        pwm.stop()
    detect = False


while True:
    t1 = Thread(target = capture())
    t1.start()
    t1.join()
    t2 = Thread(target = control())
    t2.start()
    t2.join()
   
GPIO.cleanup()
