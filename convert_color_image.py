# Convert Color Image To Gray scale and To Binary
from PIL import Image
import cv2
import numpy as np
img=cv2.imread('gh.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #converting to gray
print(np.array(gray))                       #print nueric arry.
im = Image.fromarray(gray)      #getting pixel arry.
im.show()                       #show this arry.
im.save("Gray.png")             #save it

#Convert the image to binary
img1=Image.open('Gray.png').convert('L')        #L for Gray, 1 for Binary
bw=img1.point(lambda x:0 if x<128 else 255,'1')
bw.show()
bw.save('New_binary.png')
