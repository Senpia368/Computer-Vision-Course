import matplotlib.pyplot as plt
import numpy as np
from numpy import fft

f = plt.imread("img6.jpg")
F = fft.fftshift(fft.fft2(f))
Fmag = np.abs(F)

plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.title("Fourier Magnitude")
plt.imshow(Fmag, cmap='gray')
plt.subplot(1,2,1)
plt.title("Log(Fourier magnitude)")
plt.imshow(np.log(Fmag), cmap='gray')
plt.show()