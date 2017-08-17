import os, sys
import numpy as np
from PIL import Image

im = Image.open("test-pattern.tif")
im_array = np.asarray(im).astype("uint16")

sobel_x = np.array([[-1,0,1],
           [-2,0,2],
           [-1,0,1]])
sobel_y = np.array([[-1,-2,-1],
           [0,0,0],
           [1,2,1]])

def applyfilter(image, filter):
    fd=filter.shape[0]
    height,width=image.shape
    new_image = np.zeros((height,width))
    for i in range(height-fd+1):
        for j in range(width-fd+1):
            new_image[i][j]=np.sum(image[i:i+fd,j:j+fd]*filter)
    return new_image

sobel_x_im = applyfilter(im_array,sobel_x).astype("uint8")

Image.fromarray(sobel_x_im).save("sobel_x.tif")
