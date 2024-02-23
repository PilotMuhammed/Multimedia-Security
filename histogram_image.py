# Histogram of Images
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# ---------creating img---------

img=np.zeros((200,200),np.uint8)
cv.rectangle(img,(100,100),(50,50),150,10)  #img,strt point,size,color value,thickness
cv.imshow("Zeroes",img)                     #window name,img
plt.hist(img.ravel(),200,[0,255])           #img (zeros) getting mtrx of pxl,histogram thickness, range of color value

# ---------Reading Grey img---------

img1=cv.imread("images.jpg")
cv.imshow("GrayScale",img1)

plt.hist(img1.ravel(),200,[0,100])
# ---------Reading RGB img---------
img2=cv.imread("RGB.jpg")
cv.imshow("ColorImage",img2)
plt.hist(img2.ravel(),256,[0,256])
#---------Split Value of Colors---------

r,g,b=cv.split(img2)
cv.imshow("r",r)
plt.hist(r.ravel(),256,[0,256])
cv.imshow("g",g)
plt.hist(g.ravel(),256,[0,256])
cv.imshow("b",b)
plt.hist(b.ravel(),256,[0,256])
plt.title('Histogram for color scale picture')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()