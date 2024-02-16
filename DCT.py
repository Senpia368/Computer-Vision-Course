import random
import numpy as np

def dctQuantization(B,Q):
    arr = np.zeros((8,8))
    y,x = np.meshgrid(np.arange(1,9,1),np.arange(1,9,1))
    for i in range(1,9):
        for j in range(1,9):
            ai = np.sqrt(1/8) if i == 1 else np.sqrt(2/8)
            aj = np.sqrt(1/8) if j == 1 else np.sqrt(2/8)
            arr[i-1,j-1] = ai * aj * np.sum(np.sum(B * np.cos(np.pi*(2*x-1)*(i-1)/16) * np.cos(np.pi*(2*y-1)*(j-1)/16)))
    return (np.array(arr/Q, dtype=int))

B = 255 * np.random.rand(8,8)
Q = 2*np.ones((8,8))

print(dctQuantization(B,Q))

