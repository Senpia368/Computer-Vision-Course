import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = 1.0 * plt.imread("img6.jpg")
filter = np.array([[-0.1250,-0.2500,-0.1250], [0,0,0], [0.1250,0.2500,0.1250]])
# filter = np.zeros((564,564))

img_y = ndimage.convolve(img, filter, mode='reflect')
img_x = ndimage.convolve(img, filter.T, mode='reflect')
img_g = np.sqrt(img_x**2 + img_y**2)

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(img_y, cmap='gray')
plt.subplot(1,3,2)
plt.imshow(img_x, cmap='gray')
plt.subplot(1,3,3)
plt.imshow(img_g, cmap='gray')


