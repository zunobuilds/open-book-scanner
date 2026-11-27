from pathlib import Path

import numpy as np

# from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance, ImageFilter

img = Image.open('test_images/test_image1.png')

def rotate_image(image,angle):
    return image.rotate(angle,expand=True)

def image_gaussian_blur(image,intensity):
    return image.filter(ImageFilter.GaussianBlur(intensity))

def illum_correction_formula(i,b):
    return (i/b)*255

def image_details(image):
    return image.size, image.format

def convert_array(array,dtype):
    return np.clip(array,0,255).astype(dtype)

def enhance_contrast(image,factor):
    return ImageEnhance.Contrast(image).enhance(factor)

def array_to_image(array):
    return (Image.fromarray(array))

folder = Path('test_images/cleaned/')
folder.mkdir(parents = True,exist_ok=True)


img = rotate_image(img,90)
print(image_details(img))

cleaned = img.crop((25,162,1090,1956)).convert('L')


blurred = image_gaussian_blur(cleaned,55)

blur_array= np.array(blurred)
cleaned_array = np.array(cleaned)

corrected_pixel_intensity_array =  illum_correction_formula(cleaned_array,blur_array)
corrected_pixel_intensity_array = convert_array(corrected_pixel_intensity_array,'uint8')

final_image = array_to_image(corrected_pixel_intensity_array)
final_image =  enhance_contrast(final_image,4)
final_image.show()
