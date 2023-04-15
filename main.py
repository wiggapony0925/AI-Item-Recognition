import cv2
import numpy as np
from gui_buttons import Buttons 

#__init__ buttons
button = Buttons()
button.add_button('person', 20,20)
button.add_button('cell phone', 20,20)
button.add_button('keyboard', 20,20)
button.add_button('remote', 20,20)
button.add_button('scissors', 20,20)

colors = buttons.color 

#opencv DNN Deep Neural Networks 
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights",
                      "dnn_model/yolov4-tiny.cfg",)
#object dection model
model = cv2.dnn_DetectionModel(net)   #pass the networks   #0 -> 225 scale
model.setInputParams(size=(320, 320), scale=1/225)#320x320 -> img
                        #320
#Classes Files
classes = []
with open("dnn_model/classes.txt", 'r') as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
print("classes id name")
print(classes)
        

#Camera Frame And Setup     ======(CAMERA)======
cap = cv2.VideoCapture(4)
#Settings
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# HD 1920 x1888 

#FUNCTIONS 
def click_button(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        polygon = np.array([[(20,20), (220,20), (220,70),(20,70)]])
        is_inside = cv2.pointPolygonTest(polygon, (x,y), False)
        if is_inside > 0:
            print("inside")
            if button_person is False:
                button_person = True
            else:
                button_person = False
            
            print("now  button is: ", button_person)
        
#Create window (BUTTON)  
cv2.namedWindow("Frame")
cv2.setMouseCallback('Frame', click_button)#function

while True:
    ret, frame = cap.read()
    
    #object dection()  #bboxes or boxes 
    (class_ids, scores, bboxes)= model.detect(frame) #class ids, score, boxess

  #display objects
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        #print(x, y, w, h)     
        class_name = classes[class_id]
    
        cv2.rectangle(frame, (x,y), (x + w, y +h), (255, 102, 102), 3) #add a button to change the color based on the background
        cv2.putText(frame, str(class_name), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 102 , 102), 2)
        
    #  ======BUTTON=======
    #cv2.rectangle(frame, (20,20), (220,70), (0, 0, 200), -1 )#button location 
    polygon = np.array([[(20,20),(220,20), (220,70),(20,70)]])
    cv2.fillPoly(frame, polygon, (0,0, 200))
    cv2.putText(frame, "Person", (30,60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255),3)
    
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)#mili second
