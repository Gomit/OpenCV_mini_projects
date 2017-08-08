import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,240)

while(True):
    _, frame = cap.read()
    
    
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)

    cv2.imshow('Original',frame)
    cv2.imshow('laplacian',laplacian)
    
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


