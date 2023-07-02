import cv2
import face_recognition

image = cv2.imread('C:/Users/Usuario/Desktop/alejandro.jpg',cv2.IMREAD_COLOR)
face_loc = face_recognition.face_locations(image)[0]
face_image_encodings = face_recognition.face_encodings(image, known_face_locations=[face_loc])[0]
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH ,500) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT ,500)
while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = cv2.flip(frame,1)
    face_locations = face_recognition.face_locations(frame)
    if face_locations != []:
        for face_location in face_locations:
            face_frame_encondings = face_recognition.face_encodings(frame,known_face_locations=[face_location])[0]
            result = face_recognition.compare_faces([face_frame_encondings],face_image_encodings)

            
            
            if result[0] == True:
                text = "Alejandro"
                color = (125, 220, 0)
            else:
                text = "Desconocido"
                color = (50, 50, 255)
            
            cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30), color, -1)
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
            cv2.putText(frame, text, (face_location[3], face_location[2] + 30), 2, 0.7,(255, 255, 255), 1)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k == 27 & 0xFF:
        break

cap.release()
cv2.destroyAllWindows()





