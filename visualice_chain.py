import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x=np.array([1,0,0,1,1,0,1,0,1])
y=np.array([1,0,1,1,0,1,0,0,1])
z=np.array([1,1,0,1,0,0,0,1,1])

translation_x=np.ones(len(x))
translation_y=np.ones(len(y))
translation_z=np.ones(len(z))

N_t=3
X_chain=np.zeros(len(x)*N_t)
Y_chain=np.zeros(len(x)*N_t)
Z_chain=np.zeros(len(x)*N_t)

for i in range(N_t):
    
    X_chain[i*len(x):(i+1)*len(x)]=translation_x*2*i+x
    Y_chain[i*len(x):(i+1)*len(x)]=0*translation_y*2*i+y
    Z_chain[i*len(x):(i+1)*len(x)]=0*translation_z*2*i+z

print(X_chain)
fig=plt.figure()
ax=fig.gca(projection='3d')

#ax.plot(x,y,z,"o-")


ax.plot(X_chain,Y_chain,Z_chain,"o-")
ax.set_ylim(0,3*(N_t-1))
ax.set_xlim(0,3*(N_t-1))
ax.set_zlim(0,3*(N_t-1))
plt.show()
