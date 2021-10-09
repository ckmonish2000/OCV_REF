import cv2 

# load image
img = cv2.imread("./assets/anja.jpg", 1)





# display image and wait until any btn is pressed to close
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()