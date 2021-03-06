#cv2 import
import cv2

#loading the cascade(cascadeleri opencv nin github sayfasında bulabilirsiniz. Cascade yükledik ve tanımladık. Hepsi birer xml dosyasıdır.)
face_cascade = cv2.CascadeClassifier('C:/Users/MERT/Desktop/Computer_Vision_A_Z_Template_Folder/Module 1 - Face Recognition/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/MERT/Desktop/Computer_Vision_A_Z_Template_Folder/Module 1 - Face Recognition/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('C:/Users/MERT/Desktop/Computer_Vision_A_Z_Template_Folder/Homework_Challenge_Solution/haarcascade_smile.xml')
upperbody_cascade = cv2.CascadeClassifier('C:/Users/MERT/Desktop/Computer_Vision_A_Z_Template_Folder/Homework_Challenge_Solution/haarcascade_upperbody.xml')

#tespit yapabilmek için fonksyion tanımlayacağız (Defining a function that will do the detections)
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
        ubody = upperbody_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ux, uy, uw, uh) in ubody:
            cv2.rectangle(roi_color, (ux, uy), (ux+uw, uy+uh), (0, 0, 150), 2)
    return frame

#open webcam
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
