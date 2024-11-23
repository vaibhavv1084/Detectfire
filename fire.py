from ultralytics import YOLO
import cvzone
import cv2
import math
import pygame  


pygame.mixer.init()

fire_alarm_sound = pygame.mixer.Sound('firealarm.mp3')


cap = cv2.VideoCapture(0)  
model = YOLO('fire.pt')


classnames = ['fire']

fire_alarm_played = False  

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)

    
    fire_detected = False
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])
            if confidence > 80:  
                fire_detected = True
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                   scale=1.5, thickness=2)

   
    if fire_detected and not fire_alarm_played:
        fire_alarm_sound.play()
        fire_alarm_played = True
    elif not fire_detected:
        fire_alarm_played = False  

    cv2.imshow('frame', frame)
    
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  
        break
    elif key == 32: 
        fire_alarm_sound.stop()  

cap.release()
cv2.destroyAllWindows()
