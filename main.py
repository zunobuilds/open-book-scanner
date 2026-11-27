from pathlib import Path

import numpy as np

# from matplotlib import pyplot as plt
from PIL import Image, ImageFilter

img = Image.open('test_images/test_image1.png')
format = img.format

def illum_correction_formula(i,b):
    return (i/b)*255

img = img.rotate(90,expand=True)

size = img.size
blur = ImageFilter.GaussianBlur(55)
print(size , format)
# plt.imshow(img)
# plt.show()
cleaned = img.crop((25,162,1090,1956)).convert('L')
# cleaned.show()
folder = Path('test_images/cleaned/')
folder.mkdir(parents = True,exist_ok=True)
blurred = cleaned.filter(blur)
# blurred.show()

blur_array= np.array(blurred)
cleaned_array = np.array(cleaned)
print(blur_array)
print(cleaned_array)
corrected_pixel_intensity_array =  illum_correction_formula(cleaned_array,blur_array)
corrected_pixel_intensity_array = np.clip(corrected_pixel_intensity_array,0,255).astype(np.uint8)

print(corrected_pixel_intensity_array.min(),corrected_pixel_intensity_array.max())
final_image = Image.fromarray(corrected_pixel_intensity_array)
final_image.show()
