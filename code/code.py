#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 12:30:35 2020

@author: rakeshsoni
"""

from clarifai.rest import ClarifaiApp
import json
import pandas 
import cv2
import os
import glob
from matplotlib import pyplot as plt

#Selecting the target folder for images
img_dir = "/Users/rakeshsoni/Desktop/ClothWrks/Task-2/Script"  
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)


#Authorization for the API
app = ClarifaiApp(api_key='9e6ba596155543829a93daafbbe95aca')
model = app.models.get('apparel')


#reading multiple images
for f1 in files:
    img = cv2.imread(f1)
    print(os.path.realpath(f1))
    imge = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imge)
    plt.xticks([]), plt.yticks([]) 
    plt.show()
    
#Image calling the API
response=[]

for f1 in files:
    img = os.path.realpath(f1)
    response.append(model.predict_by_filename(img))
    

response_json = json.dumps(response) #converts the list to string


#Converting to JSON
json_parsed = json.loads(response_json)

json_m=[]

for i in json_parsed:
    json_m.append(i['outputs'][0]['data'])

    
json_m
final_json = json.dumps(json_m)


#Converting to CSV
df=pandas.read_json(final_json)
df.to_csv('test.csv',index=None)
print("Successfuly converted to CSV")


#Sending the csv using shopify's API