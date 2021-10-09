import cv2 

# load image
img = cv2.imread("./assets/anja.jpg", 1)

# resize
image2 = cv2.resize(img,(0,0),fx=2,fy=2)
image2 = cv2.resize(img,(1000,1000),fx=2,fy=2)

# rotate
image3 = cv2.rotate(img,cv2.ROTATE_180)

# write image

cv2.imwrite("newimg.jpg",image3)

# display image and wait until any btn is pressed to close
cv2.imshow('img',image3)
cv2.waitKey(0)
cv2.destroyAllWindows()