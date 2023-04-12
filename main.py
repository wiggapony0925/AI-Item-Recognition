import cv2

#opencv DNN Deep Neural Networks 
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights",
                      "dnn_model/yolov4-tiny.cfg",)
#object dection model
model = cv2.dnn_DetectionModel(net)   #pass the networks   #0 -> 225 scale
model.setInputParams(size=(320, 320), scale=1/225)#320x320 -> img

#Classes Files
classes = []
with open("dnn_model/classes.txt", 'r') as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
print("classes id name")
print(classes[0])
        

#Camera Frame And Setup
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    #object dection()  #bboxes or boxes 
    (class_ids, scores, bboxes)= model.detect(frame) #class ids, score, boxess

  #display objects
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        print(x, y, w, h)     
        class_name = classes[class_id]
    
        cv2.rectangle(frame, (x,y), (x + w, y +h), (255, 102, 102), 3) #add a button to change the color based on the background
        cv2.putText(frame, str(class_name), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 102 , 102), 2)
        
    print("class ids", class_ids)
    print("score", scores)
    print("binding boxes", bboxes)
        
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)#mili second
