import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480)

fourcc1 = cv2.cv.CV_FOURCC(*'DIVX')
#fourcc2 = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('videos/output.avi',fourcc1, 20.0, (640,480))

while(True):
    retval, frame = cap.read()
    if retval==True:

        # write the frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()


"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    retval, image = cap.read()
    
    
    #gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('image',image)
    #cv2.imshow('gray',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""


