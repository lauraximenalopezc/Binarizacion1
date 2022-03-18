#Librería
import cv2
from cv2 import imshow
import numpy as np
"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="stitch"
#Lectura de imagen
img= cv2.imread(imgText+'.jpg')
imshow('Imagen Original',img)

#Imagen escala de grises
imgGrau= cv2.imread(imgText+'.jpg',0)
imshow('Grises',imgGrau)

#Binarización
ret,tresh=cv2.threshold(imgGrau,150,200,cv2.THRESH_BINARY)
imshow('Binarizada',tresh)
#Binarización adaptativo
th1=cv2.adaptiveThreshold(imgGrau,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,40)
th2=cv2.adaptiveThreshold(imgGrau,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,40)
imshow('Promedio',th1)
imshow('Gaussiano',th2)


#Binarización Otsu
ret,th3=cv2.threshold(imgGrau,150,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
imshow('Otsu',th3)

#Letras
#print(pytesseract.image_to_string(th3))

kernel = np.ones((5,5), np.uint8)
 
# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
img_erosion = cv2.erode(th3, kernel, iterations=1)
img_dilation = cv2.dilate(th3, kernel, iterations=1)
 
#cv2.imshow('Erosion', img_erosion)
#cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
