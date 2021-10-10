import cv2

image = cv2.imread("./assets/download.jpg")
image2 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(image2,1.1,4)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(image2, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv2.imshow('detect',image2)
cv2.waitKey(0)