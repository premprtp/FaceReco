import cv2

face_cascade = cv2.CascadeClassifier("/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/venv/Lib/site-packages/cv2/data/haarcascade_eye.xml")

video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()
    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = video_data[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow("video_live", video_data)
    if cv2.waitKey(1) == 27:
        break
video_cap.release()
cv2.destroyAllWindows()











""" import cv2

face_cap = cv2.CascadeClassifier("D:/Github_repo/Project/FaceReco//venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(video_data, (x,y),(x+w, y+h), (0,255,0),2)
    cv2.imshow("video_live", video_data)
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release() """