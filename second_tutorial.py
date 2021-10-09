import cv2

# read
image = cv2.imread('./assets/anja.jpg',-1)

# type of image
print(type(image))

# image shape
print(image.shape)

# copy part of the array and paste it somewhere

tag = image[300:400,500:600]
image[200:300,600:700] = tag

# basically ur performing array manipulation by resetting valuess in that array position

# display
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
