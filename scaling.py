import cv2
import numpy as np 
import math

img=cv2.imread("Figure_75.png")
print(type(img))  #img store in array
x_sf=int(input("enter the scaling factor for x axis:"))
y_sf=int(input("enter the scaling factor for y axis:"))
height,width,channel=img.shape #image is a 3-dim array,the shape returns no of rows and no of columns and no of channels
print(height,width,channel)
new_img_ht=y_sf*height
new_img_wd=x_sf*width
output_img=np.zeros((new_img_ht,new_img_wd,channel), dtype=np.uint8)
print(output_img.shape)

for x in range(new_img_wd):
    for y in range(new_img_ht):
        xp=math.floor(x*x_sf)
        yp=math.floor(y*y_sf)
        if(0<=xp<new_img_wd and 0<=yp<new_img_ht ):
            output_img[yp,xp]=img[y,x]
cv2.imshow("img",output_img)
cv2.waitKey(0)