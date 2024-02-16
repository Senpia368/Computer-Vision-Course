import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = 1.0 * plt.imread("img4.jpg")

img_sobel = ndimage.sobel(img)



plt.imshow(img_sobel)