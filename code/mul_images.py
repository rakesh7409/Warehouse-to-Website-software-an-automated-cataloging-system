#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:13:34 2020

@author: rakeshsoni
"""

import cv2
import os
import glob
from matplotlib import pyplot as plt

img_dir = "/Users/rakeshsoni/Desktop/ClothWrks/Task-2/Script"  
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)

for f1 in files:
    img = cv2.imread(f1)
    print(os.path.realpath(f1))
    imge = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imge)
    plt.xticks([]), plt.yticks([]) 
    plt.show()
   
    
   