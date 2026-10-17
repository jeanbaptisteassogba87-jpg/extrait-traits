import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, filters


def longueurs_suites(ligne):
    """Pour chaque pixel, renvoie la longueur de la suite de True qui le contient (0 si fond)."""
    n = len(ligne)
    res = np.zeros(n, dtype=int)
    i = 0
    while i < n:
        if ligne[i]:
            j = i
            while j < n and ligne[j]:
                j += 1
            res[i:j] = j - i
            i = j
        else:
            i += 1
    return res


# Chargement : change le nom pour tester (test.png ou photo.png)
img = io.imread("images/photo.png")

# Binarisation : seuil local pour la couleur, seuil fixe pour le rectangle gris
if img.ndim == 3:
    gray = color.rgb2gray(img[:, :, :3])
    binaire = gray < filters.threshold_local(gray, 31, offset=0.02)
else:
    gray = img
    binaire = gray < 128

# Réglages (un seul à la fois quand tu testes)
LONGUEUR_MIN = 50     # longueur minimale d'un trait
EPAISSEUR_MAX = 4     # épaisseur maximale d'un trait

H, W = binaire.shape

# Longueur de la suite horizontale et verticale de chaque pixel
suite_h = np.array([longueurs_suites(binaire[y]) for y in range(H)])
suite_v = np.array([longueurs_suites(binaire.T[x]) for x in range(W)]).T

# Trait horizontal : long horizontalement, fin verticalement
sortie_h = (suite_h >= LONGUEUR_MIN) & (suite_v <= EPAISSEUR_MAX)
# Trait vertical : long verticalement, fin horizontalement
sortie_v = (suite_v >= LONGUEUR_MIN) & (suite_h <= EPAISSEUR_MAX)

sortie_hv = sortie_h | sortie_v

# Affichage : figure à fond blanc, traits blancs sur fond noir
fig, axes = plt.subplots(2, 3)

axes[0, 0].set_title("Image de départ")
axes[0, 0].imshow(img, cmap="gray")

axes[0, 1].set_title("Binarisation")
axes[0, 1].imshow(binaire, cmap="gray")

axes[0, 2].set_title("Verticaux seuls")
axes[0, 2].imshow(sortie_v, cmap="gray")

axes[1, 0].set_title("Horizontaux seuls")
axes[1, 0].imshow(sortie_h, cmap="gray")

axes[1, 1].set_title("Verticaux + horizontaux")
axes[1, 1].imshow(sortie_hv, cmap="gray")

for ax in axes.flat:
    ax.axis("off")

plt.show()

# Sauvegarde du résultat final (blanc = trait, noir = fond)
io.imsave("traits.png", (sortie_hv * 255).astype(np.uint8))
