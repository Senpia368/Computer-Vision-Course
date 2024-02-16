import numpy as np 
from math import sin, cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# 3D cube coordinates (homogenous)
P = np.array([[0,0,0,1],[1,0,0,1],[1,1,0,1],[0,1,0,1],[0,0,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1]])

# Transformation matrix
Rx = np.radians(30) # rotation radians
Ry = np.radians(30)
Rz = np.radians(0)
Tx = 0 # translation
Ty = 0
Tz = 100
f = 1

K = np.array([[f,0,0],[0,f,0],[0,0,1]]) # intrinsic matrix
RMx = np.array([[1, 0, 0], [0,cos(Rx),-sin(Rx)], [0,sin(Rx),cos(Rx)]])
RMy = np.array([[cos(Ry),0,sin(Ry)], [0,1,0], [-sin(Ry),0,cos(Ry)]])
RMz = np.array([[cos(Rz),-sin(Rz),0],[sin(Rz),cos(Rz),0],[0,0,1]])
RM = RMx @ RMy @ RMz
M = np.zeros((3,4))
M[0,3] = Tx
M[1,3] = Ty
M[2,3] = Tz
M[0:3,0:3] = RM # extrinsic matrix

# perspective projection

p = K @ M @ np.transpose(P) # projection (homogenous coordinates)
x = p[0,:]/p[2,:]
y = p[1,:]/p[2,:]

plt.plot(x,y)
plt.show()
