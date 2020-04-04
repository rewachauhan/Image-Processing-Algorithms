import cv2
import numpy as np 
import math

img=cv2.imread("Figure_75.png")
print(type(img))  #img store in array
angle=float(input("enter the angle of rotation in degrees : "))
angle= angle*(math.pi/180)
height,width,channel=img.shape #image is a 3-dim array,the shape returns no of rows and no of columns and no of channels
#centers being determined for the reference while rotating the image
xcenter=width/2  
ycenter=height/2
print(height,width,channel)
output_img=np.zeros((height,width,channel), dtype=np.uint8)
print(output_img.shape)

for x in range(width):
    for y in range(height):
        #acc to rotation matrix
        xp=int((x-xcenter)*math.cos(angle)-(y-ycenter)*math.sin(angle)+xcenter)
        yp=int((x-xcenter)*math.sin(angle)+(y-ycenter)*math.cos(angle)+ycenter)
        if(0<=xp<width and 0<=yp<height ):
            output_img[yp,xp]=img[y,x]
cv2.imshow("img",output_img)
cv2.waitKey(0)