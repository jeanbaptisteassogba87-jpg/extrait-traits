from scipy import ndimage 
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color

H = np.array([
    [-1, -1, -1],
    [2,   2,  2],
    [-1, -1, -1]
])
img = io.imread("images/maison.jpg")
imggray = color.rgb2gray(img)
resultat = ndimage.consolve(imggray,H)
print(resultat.shape)
print(resultat.max())
print(resultat.min())
print(H.shape)
print(imggray.shape)
print(imggray)

#plt.imshow(imggray)
#plt.show()
