import cv2
import numpy as np
import os
import time
from datetime import datetime
import pywhatkit

print("""

             U _____ u  _        ____   U  ___ u  __  __  U _____ u   
 __        __\| ___"|/ |"|    U /"___|   \/"_ \/U|' \/ '|u\| ___"|/   
 \"\      /"/ |  _|" U | | u  \| | u     | | | |\| |\/| |/ |  _|"     
 /\ \ /\ / /\ | |___  \| |/__  | |/__.-,_| |_| | | |  | |  | |___     
U  \ V  V /  U|_____|  |_____|  \____|\_)-\___/  |_|  |_|  |_____| _  
.-,_\ /\ /_,-.<<   >>  //  \\  _// \\      \\   <<,-,,-.   <<   >>(") 
 \_)-'  '-(_/(__) (__)(_")("_)(__)(__)    (__)   (./  \.) (__) (__)"  

""")
print()
print()
time.sleep(2)
print("""

  _____    _            _   _  __        __     __                       _  __ 
 |_   _|  | |          | | (_)/ _|       \ \   / /                      | |/ _|
   | |  __| | ___ _ __ | |_ _| |_ _   _   \ \_/ /__  _   _ _ __ ___  ___| | |_ 
   | | / _` |/ _ \ '_ \| __| |  _| | | |   \   / _ \| | | | '__/ __|/ _ \ |  _|
  _| || (_| |  __/ | | | |_| | | | |_| |    | | (_) | |_| | |  \__ \  __/ | |  
 |_____\__,_|\___|_| |_|\__|_|_|  \__, |    |_|\___/ \__,_|_|  |___/\___|_|_|  
                                   __/ |                                       
                                  |___/                                        
""")
print("Starting Faceial Recognition......")

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
devansh_model = cv2.face_LBPHFaceRecognizer.create()
devansh_model.read('devansh_model.yml')
flag = 0

def face_detector(img, size=0.5):
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    
    image, face = face_detector(frame)
    
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        results = devansh_model.predict(face)
        
        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'
            
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
        
        if confidence >= 90:
            cv2.putText(image, "Hello Devansh", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )
            flag = 1
            break
            
         
        else:
            
            cv2.putText(image, "I dont know, how r u", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )

    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "looking for face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass
        
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cv2.destroyAllWindows()    


if flag == 1:
    while True:
        print("Press 1 to launch a VPC over AWS cloud")
        print("Press 2 to send a WhatsApp message")
        print("Press 3 to exit")
        demand = int(input("Enter the task you want to proceed:"))
        if demand == 1:
            os.system("terraform apply")
            os.system("terraform apply -auto-approve")
        elif demand == 2:
            phno = input("Enter mobile no:")
        #print(phno)
            now = datetime.now()
            hours = int(now.strftime("%H"))
            type_hour = type(hours)
        #print(type_hour)
        #print("Current Time =", hours)
            minutes = int(now.strftime("%M")) + 1
            type_minutes = type(minutes)
        #print(type_minutes)
        #print("Current Time =", minutes)
            pywhatkit.sendwhatmsg(phno , "Hey bud ,  we have completed the task ",hours,minutes)
        elif demand==3:
            break
        else:
            print("Not a valid Option")
            
else:
    print("Unidentified user trying to login")
    
