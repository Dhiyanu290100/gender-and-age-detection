# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:27:33 2020

@author: Lithin
"""

import urllib.request
import cv2
import numpy as np
import time
URL = "http://192.168.43.210:8080"
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    cv2.imshow('IPWebcam',img)
    
    if cv2.waitKey(1):
        break