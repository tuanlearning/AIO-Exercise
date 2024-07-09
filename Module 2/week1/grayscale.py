import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Using Lightness method
img = mpimg.imread('.Module 2\week1\dog.jpg')
gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2

# Using Average method
gray_img_02 = np.mean(img, axis=2)

# Using Luminosity method
gray_img_03 = img[:, :, 0] * 0.21 + img[:, :, 1] * 0.72 + img[:, :, 2]*0.07
