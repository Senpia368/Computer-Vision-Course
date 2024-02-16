import matplotlib.pyplot as plt
import numpy as np
f = plt.imread('img6.jpg')
F = np.abs(f)

plt.figure(figsize=(600,600))
plt.subplot(1,2,1)
plt.imshow(F, cmap='gray')
plt.show()