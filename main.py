
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

img = io.imread("images/test.png")
print(img.shape)
print(img.dtype)
print(img[0,0])
