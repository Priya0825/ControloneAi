import os
import cv2
from glob import glob

if __name__ == "__main__":
    data = glob(os.path.join("faces", "*.jpeg"))
    face_cascade = cv2.CascadeClassifier("Task 1/haarcascade_frontalface_default.xml") # Enter the path of xml file

    for path in data:
        image = cv2.imread(path, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray,1.2,4)
        for (x, y, w, h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        
        cv2.imshow("Face Detection",image)
        k = cv2.waitKey(0)
        if k == ord('q'):
            cv2.destroyAllWindows()