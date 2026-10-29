import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color

img = io.imread("images/maison.jpg")
imgray = color.rgb2gray(img)
print('imgray max{} , img max{}'.format(imgray.max(), img.max()))
"""
plt.subplot(1,3,1)
plt.imshow(img[:,:,0], cmap="gray")
plt.subplot(1,3,2)
plt.imshow(img[:,:,1], cmap="gray")
plt.subplot(1,3,3)
plt.imshow(img[:,:,2], cmap="gray")
plt.show()
#"""
