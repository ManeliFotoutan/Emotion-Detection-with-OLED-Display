import cv2
from deepface import DeepFace
import serial
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)  # Replace 'COM3' with your Arduino port
time.sleep(2)  # Give some time for the connection to establish

while True:
    ret, frame = cap.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = rgb_frame[y:y + h, x:x + w]

        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

        emotion = result[0]['dominant_emotion']

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        arduino.write((emotion + '\n').encode())


    cv2.imshow('Real-time Emotion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

arduino.close()
