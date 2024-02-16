import matplotlib.pyplot as plt
import numpy as np
from numpy import fft

f = plt.imread("img6.jpg")
[ydim, xdim] = f.shape
win = np.outer(np.hanning(ydim), np.hanning(xdim))
win = win / np.mean(win)
F = fft.fftshift(fft.fft2(f*win))
Fmag = np.abs(F)

plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.title("windowed image")
plt.imshow(f*win, cmap='gray')
plt.subplot(1,2,1)
plt.title("Log(Fourier magnitude)")
plt.imshow(np.log(Fmag), cmap='gray')
plt.show()