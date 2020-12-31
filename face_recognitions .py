# -*- coding: utf-8 -*-
"""Face Recognitions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eX_HDJOhbNYdP65cfpD_mwZTod0yJDrm
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import os
import fnmatch
from matplotlib import pyplot as plt
# %matplotlib inline

pip install face_recognition

import face_recognition as fr

#  from google.colab import drive
# drive.mount('/content/drive')

import zipfile
with zipfile.ZipFile('/content/drive/MyDrive/trainset.zip', 'r') as zip_ref:
    zip_ref.extractall('trainsetz')

face = fr.load_image_file('/content/trainsetz/trainset/0001/0001_0000262/0000011.jpg')
plt.imshow(face)
plt.show()

script = fr.load_image_file('/content/trainsetz/trainset/0001/0001_0000262/0001_0000262_script_2.jpg')
plt.imshow(script)
plt.show()

faceLoc = fr.face_locations(face)    #locate where face is in picture

encodes = fr.face_encodings(face, faceLoc)  #apply face encoding 

encode = fr.face_encodings(script)[0]    #apply encoding to test image

matches = fr.compare_faces(encodes, encode) #match the two images and check same person or not
print(matches)

encodesCurFrame = []
encode = []
matches = []
i = 0

for root,_,files in os.walk('/content/trainsetz/trainset.csv'):
    t=0
    f=0
    for filename in files: 
        matches = []
        file = os.path.join(root,filename)
        if fnmatch.fnmatch(file,'*script*'):
            label = file
            #print("label=",label)
            test = fr.load_image_file(label)        
            encode = fr.face_encodings(test)[0]
                    
        else:
            image = file
            #print("image=",image)
            img = fr.load_image_file(image)
            facesCurFrame = fr.face_locations(img)
            encodesCurFrame = fr.face_encodings(img, facesCurFrame)
        
        #print(file)
    matches = fr.compare_faces(encodesCurFrame, encode)  
    if matches == []:
        continue
    else:      
        i+=1
        print(matches,i)
        for m in matches:
            if m==True:
                t+=1
            else:
                f+=1

    print("acc =", t/(t+f))

