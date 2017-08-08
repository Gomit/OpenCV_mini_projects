import cv2
import numpy as np

img_rgb = cv2.imread('images/opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('images/opencv-template-for-matching.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
cv2.imwrite('res.png',res)
print(res[0].size)
threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)

cv2.imshow('res',res)
cv2.imshow('template',template)
cv2.imwrite('img_gray.png',img_gray)
#cv2.imwrite('res.png',res)
print(loc[0])

cv2.waitKey(0)
cv2.destroyAllWindows()

