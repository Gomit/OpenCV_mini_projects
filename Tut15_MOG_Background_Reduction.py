import numpy as np
import cv2

cap = cv2.VideoCapture('videos/people-walking.mp4')

#cap = cv2.VideoCapture(0)

#cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480)

fgbg = cv2.BackgroundSubtractorMOG()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()