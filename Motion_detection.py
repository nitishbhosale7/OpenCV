import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cap = cv.VideoCapture('vtest.avi')

ret, frame1 = cap.read()  #here wew are now reading two frames , to find the difference between them
ret, frame2 = cap.read()
while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)  # This gives us the absolute difference between the frames
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY) # we convert the diff image into the grayscale image to easliy detect the countor
    blur = cv.GaussianBlur(gray, (5, 5), 0) #here we are blurring means smoothinening the image
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY) #here we are finding the threhold
    dilated = cv.dilate(thresh, None, iterations=3)
    countours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for countour in countours:
        (x,y,w,h) = cv.boundingRect(countour)   # this methods returns the x and y cordinate and width and height pf the moving countor
        if cv.contourArea(countour) < 700:
            continue
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)
        cv.putText(frame1 , 'status : {}'.format('movement'),(10,20),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    #cv.drawContours(frame1, countours, -1,(0,255,0),2)

    cv.imshow('new', frame1) # here we are displaying the frame 1 , so we are assigning the value of the frame 1 to frame 2
    frame1 = frame2
    ret, frame2 = cap.read() # now we are again reading the new image into frame1 , and we will compare it with previous as we loops againb

    if cv.waitKey(40) == 27:
        break

cv.destroyAllWindows()
cap.release()
