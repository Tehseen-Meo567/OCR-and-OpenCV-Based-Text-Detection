import numpy as np
import cv2
import matplotlib.pyplot as plt
import easyocr

image_path= 'caution.jpg'
img = cv2.imread(image_path)
reader= easyocr.Reader(['en'],gpu= False)
a= reader.readtext(image_path)
print(a)

#top_left = tuple(a[0][0][0])
#bottom_right = tuple(a[0][0][2])
#text = a[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX


for detection in a: 
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    img = cv2.rectangle(img,(top_left),(bottom_right),(0,255,0),5)
    txt = cv2.putText(img,text,top_left, font,0.65,(255,0,0),2,cv2.LINE_AA)
plt.figure(figsize=(10,40))      
plt.imshow(img)
plt.show()