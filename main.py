import cv2

#opencv DNN Deep Neural Networks 
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights",
                      "dnn_model/yolov4-tiny.cfg",)
#object dection model
model = cv2.dnn_DetectionModel(net)   #pass the networks   #0 -> 225 scale
model.setInputParams(size=(320, 320), scale=1/225)#320x320 -> img


#Camera Frame And Setup
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    #object dection()  #bboxes or boxes 
    (class_ids, score, bboxes)= model.detect(frame) #class ids, score, boxess
    print("class ids", class_ids)
    print("score", score)
    print("binding boxes", bboxes)
        
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)#mili second
