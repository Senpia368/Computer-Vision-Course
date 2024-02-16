import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


N = 256
im = np.zeros((N,N,3))

for i in range(0,N):
    im[i,:,0] = i*0.0039
    im[i,:,1] = 1 - i*0.0039
    im[i,:,2] = 1


plt.imshow(im)



