import cv2

#opencv DNN Deep Neural Networks

#Camera Frame And Setup
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)
    cv2.waitKey(1)#mili second
