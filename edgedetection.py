import cv2
import numpy as np 
import matplotlib.pyplot as plt
import math

img=cv2.imread("Figure_75.png",cv2.IMREAD_GRAYSCALE)
fx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
fy=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
def conv2d(image,filter):
    height=image.shape[0]
    width=image.shape[1]
    output=np.zeros((height,width))
    for i in range(width-2):
        for j in range(height-2):
            output[j,i]=(filter*image[j:j+3,i:i+3]).sum()
    return output
X=conv2d(img,fx)/9
Y=conv2d(img,fy)/9
out=np.sqrt(np.power(X,2)+np.power(Y,2))
out=(out/np.max(out))*255
plt.imshow(out,cmap="gray",interpolation="bicubic")
plt.show()
