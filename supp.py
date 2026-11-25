import matplotlib.pyplot as plt
from scipy.ndimage import median_filter , uniform_filter
from skimage import color, data,util

photo_couleur = data.astronaut()
photo_grise = color.rgb2gray(photo_couleur)
photo_bruitee =  util.random_noise(photo_grise, mode="s&p", amount=0.05)
img_debruitee = median_filter(photo_bruitee, size=3)
img_moyen = uniform_filter(photo_bruitee, size=3)

fig , axes = plt.subplots(2,2, figsize=(15,15))

axes[0,0].imshow(photo_grise, cmap="gray")
axes[0,0].set_title("1- Originale(gris)")

axes[0,1].imshow(photo_bruitee, cmap="gray")
axes[0,1].set_title("2- Bruitée(Poivre & Sel)")

axes[1,0].imshow(img_debruitee, cmap="gray")
axes[1,0].set_title("3- Nettoyée(Filtre Médian 3*3)")

axes[1,1].imshow(img_moyen, cmap="gray")
axes[1,1].set_title("3- Nettoyée(Filtre Moyenneur 3*3)")

plt.show()
