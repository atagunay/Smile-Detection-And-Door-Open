# Smile Detection with Face Detection And Opening The Door with Servo Motors
Note: The operability of this project has been tested on windows10/11, ubuntu and raspberry pi 3.

## Requirements
1. Raspberry Pi
2. Servo Motor
3. Camera

## Code Analysis

### a. Import Libs
1. numpy and cv2 used for face detection.
2. Rpi.GPIO used for servo motor.
3. threading and time used for multi thread operations.

```python
import numpy as np
import cv2
import time
import RPi.GPIO as GPIO
from threading import Thread
```

### b. Load Face Informations

```python
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
```

### c. Start the Camera

```python
cap = cv2.VideoCapture(0)
```

### d. Define Global Variable For Used By Threads

```python
detect = False
```

### e. Capture Thread
If a smiling is detected, the global variable is set true

```python
 for i in smile:
  if len(smile)>1:
    print("guldu")
    detect = True
    break
```

### f. Control Thread
If global variable is true, servo motor runs

```python
 for i in smile:
  if len(smile)>1:
    print("guldu")
    detect = True
    break
```

### g. Synchronization Of Threads
Threads are made to run one after the other and wait for each other

```python
while True:
    t1 = Thread(target = capture())
    t1.start()
    t1.join()
    t2 = Thread(target = control())
    t2.start()
    t2.join()
```








