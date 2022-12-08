#Installed Programs: Python 3.10.6 (x64), Tesseract OCR 5.2.0
#Installed Libraries: django, pyautogui, opencv-python, numpy, pytesseract, google, googlesearch-python

import os
from itertools import count
from pydoc import stripid
import pyautogui
import cv2
import numpy as np
import webbrowser
from PIL import Image
from pytesseract import *
from turtle import title
from googlesearch import search

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
# Thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Dilation
def dilate(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
# Erosion
def erode(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

# Opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

# Resizing image
def resize_img(image):
    return cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

# This part finds the user's desktop location
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
temp="\img2txt\Find.png"
location=desktop+temp

# This part reads the image
image_read = cv2.imread(location)

# Pre-Processing Commands

#image_read = resize_img(image_read)
#gray = get_grayscale(image_read)
#noise = remove_noise(image_read)
#thresh = thresholding(image_read)
#dilation = dilate(gray)
#erosion = erode(dilation)


# This part gets the text from image as string and splits to array.
string_output = pytesseract.image_to_string(image_read)
string_array = string_output.split()

# This part removes non alphanumeric values.
counter = 0
for temp in string_array:
    string_temp = ''.join(ch for ch in temp if ch.isalnum())
    string_array[counter] = string_temp
    counter += 1

# This part joints array elements with plus in between.
string_search = "+"
string_search = string_search.join(string_array)
string_search += '+IMDB'


# This part searches the string and gets the first link.
for temp in search(string_search, tld="co.in", num=10, stop=1, pause=2):
    url=temp

url_array = url.split('/')

# This part checks the link that is longer than expected
if  url_array[5] != '':
    url_array[5] = ''
    print("not null")
    if len(url_array) > 6:
        count = 6
        print("long")
        while count < len(url_array):
            url_array.pop(count)
            count += 1
    url_join = "/".join(url_array)
    url = url_join


#url = 'https://www.google.com/search?q=XYZ'
#url = url.replace("XYZ", string_search)

# This part opens the link.
webbrowser.open(url)