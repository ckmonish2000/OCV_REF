import cv2
import numpy as np

# camera

cap = cv2.VideoCapture(0)


while True:
  ret, frame = cap.read()
  
  # height of frame 
  width = int(cap.get(3))
  height = int(cap.get(4))

  frame2 = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
  image = np.zeros(frame.shape,np.uint8)
  
  image[:height//2,:width//2] = frame2
  image[height//2:,:width//2] = cv2.rotate(frame2,cv2.ROTATE_180)
  image[:height//2,width//2:] = cv2.rotate(frame2,cv2.ROTATE_180)
  image[height//2:,width//2:] = frame2

  cv2.imshow('frame',image)

  if cv2.waitKey(1) == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()