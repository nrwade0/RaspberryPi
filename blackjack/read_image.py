# -*- coding: utf-8 -*-
"""
Project Euler #1
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


#import numpy as np
import cv2 as cv

# Load an color image
cv.namedWindow("image")
img = cv.imread('data/img008.jpg')
cv.imshow("image",img)

cv.waitKey(1000) # 5 sec delay before image window closes
cv.destroyWindow("image")


print('thats half the budget man')

print(cv.__version__)

