import cv2

#cascadeclassifier object
face_cascade = cv2.CascadeClassifier("C:\\Users\\hp\\Documents\\OpenCV\\haarcascade_frontalface_default.xml")

#reading colored image
img = cv2.imread ("C:\\Users\\hp\Documents\\OpenCV\\group.jpeg",1)

#converting image into gray-scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#finding co-ordinates of the face
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)

print(type(faces))
print(faces)

#co-ordinates of face 
for w, x, y, z in faces:
    img = cv2.rectangle(img, (w,x), (w+y,x+z),(0,255,0),3)

#resize image
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

#display image
cv2.imshow ("Group-photo",resized)

#Close window
cv2.waitKey(0)
cv2.destroyAllWindows()