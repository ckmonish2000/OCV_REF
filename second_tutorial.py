import cv2

# read
image = cv2.imread('./assets/anja.jpg',-1)

# type of image
print(type(image))

# image shape
print(image.shape)


# display
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
