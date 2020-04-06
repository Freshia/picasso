import cv2
import numpy as np
import math
import matplotlib as plt
import imutils


img =cv2.imread('my_drawing.png',cv2.IMREAD_GRAYSCALE)
width = np.size(img, 1)
height = np.size(img, 0)
img_array = []

def pre_process_image(img):
    resized_image = imutils.resize(img,200,200)
    ret,mask = cv2.threshold(resized_image,125,255,cv2.THRESH_BINARY_INV)
    mask_inv=cv2.bitwise_not(mask)
    cv2.imshow('invmsk',mask_inv)
    resized_image = cv2.resize(mask_inv,(8,8))
    cv2.imshow('',resized_image)

    return resized_image

def image_to_array(resized_image):
    #changing pixels to match dataset
    scale = 255/16
    for i in range(8):
        for j in range(8):
            fraction = resized_image[i][j]/scale
            #rounding off
            if math.modf(fraction)[0] > 0.5:
                resized_image[i][j] = (math.trunc(fraction)+1)
            else:
                resized_image[i][j] = math.trunc(fraction)
            img_array.append(resized_image[i][j])
    
    return img_array

resized_image = pre_process_image(img)
img_array = image_to_array(resized_image)
print(img_array)
#img_array = np.array(img_array)
cv2.waitKey()
cv2.destroyAllWindows()