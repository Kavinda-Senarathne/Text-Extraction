# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 09:01:38 2020

@author: Kavinda
"""
#You need to use iamges with white background
# Import modules
from PIL import Image
import pytesseract

# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Create an image object of PIL library
image = Image.open("test1.jpg")

# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')

# Print the text
print(image_to_text)