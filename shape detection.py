import numpy as np
from matplotlib import pyplot
import cv2 as cv

shape = cv.imread('shapes.PNG')
gray = cv.cvtColor(shape, cv.COLOR_BGR2GRAY)
_, threshold = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    '''
    The function cv::approxPolyDP approximates a curve or a polygon with another curve/polygon with less
    .   vertices so that the distance between them is less or equal to the specified precision. It uses the
    .   Douglas-Peucker algorithm
    it gives the number of approximate polygonal curve in the countor so accroding to the number of cureves we can detemrmine
    the shape of the object , Now if it returns 3 curves we can determine that 3 closed cureves makes triangle in this way 
    '''
    cv.drawContours(shape, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0] +15
    y = approx.ravel()[1] -20

    if len(approx) == 3:
        print('its a traingle')
        cv.putText(shape, 'Traingle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0 , 255))

    elif len(approx) == 4:
        x, y, w, h = cv.boundingRect(approx)
        aspect_ratio = float(w) / h
        print(aspect_ratio)
        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            print('its a sqaure')
            cv.putText(shape, 'square', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))

        else:
            print('its a rectangle')
            cv.putText(shape, 'rectangle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))

    elif len(approx) == 5:
        print('its a pentagon')
        cv.putText(shape, 'pentagon', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))

    elif len(approx) == 10:
        print('its a star')
        cv.putText(shape, 'star', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))

    else:
        print('its a circle')
        cv.putText(shape, 'circle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))

cv.imshow('shape', shape)
cv.waitKey(0)
cv.destroyAllWindows()
