"""
import cv2
import numpy as np

img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainsvmimage.png')

#add = img1+img2
#add = cv2.add(img1,img2)

weighted = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
import cv2
import numpy as np

# Load two images
img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainlogo.png')

# Save the size of the logo into variables
rows,cols,channels = img2.shape

# I want to put logo on top-left corner, So we create a ROI
roi = img1[0:rows, 0:cols ]
cv2.imshow('roi',roi)
# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

# Create inverse of mask
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI "Region of Image"
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Paste region of logo onto region of image.
dst = cv2.add(img1_bg,img2_fg)

# Set new logo image "dst" equal to upper-right region of cluster image 
img1[0:rows, 0:cols ] = dst

# Paste result.
cv2.imshow('6',img1)

#cv2.imshow('1',mask)
#cv2.imshow('2',mask_inv)
#cv2.imshow('3',img1_bg)
#cv2.imshow('4',img2_fg)
#cv2.imshow('5',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
