# -*- coding: utf-8 -*-
"""AVD2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xg9icoQFZTgrMYEk5RdvXuHYI2ALgpcI

AVD 2
Gustavo Lima Carvalho (202010404)
"""

# Importação das bibliotecas necessárias (OpenCV, NumPy, Dlib, etc...)
from PIL import Image
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import dlib

# Carregamento do detector de faces
face_detector = dlib.get_frontal_face_detector()

# Carregamento da imagem q será utilizada como exemplo
img = cv2.imread('image.jpg')

# Detecção dos rostos da imagem com sua respetiva marcação em 'img'
detected_face = face_detector(img, 1)
for face in detected_face:
  l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
  cv2.rectangle(img, (l,t), (r, b), (0,255,255), 2)

#-----------------------------------------------------------------------------

# Carregamento do modelo de marcações faciais
point_detector = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Carregamento da imagem que será utilizada como exemplo
img2 = cv2.imread('image.jpg')

# Detecção dos marcos faciais com marcações circulares vermelhas em 'img2'
detected_face = face_detector(img2, 1)
for face in detected_face:
  detected_points = point_detector(img2, face)

  for detected_points in detected_points.parts():
    cv2.circle(img2, (detected_points.x, detected_points.y), 2, (0,0,255), 1)

#-----------------------------------------------------------------------------

# Carregamento da imagem que será utilizada como exemplo
img3 = cv2.imread('image.jpg')

# Gerando circulo centrado no ponto médio das faces detectadas em 'img3'
detected_face = face_detector(img3, 1)
for face in detected_face:
  l, t, r, b = face.left(), face.top(), face.right(), face.bottom()

  cv2.circle(img3, ((l+r)//2, (t+b)//2), (r-l)//2, (0,255,0))

#-----------------------------------------------------------------------------

# Exibição de todas as imagens obtidas 
cv2_imshow(img)
cv2_imshow(img2)
cv2_imshow(img3)