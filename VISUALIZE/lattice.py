import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


xi=np.array([1,1,0])
xj=np.array([0,1,1])
xk=np.array([1,0,1])

r0=np.array([0,0,0])*2
r1=np.array([0.25,0.25,0])*2
r2=np.array([0.25,0,0.25])*2
r3=np.array([0,0.25,0.25])*2


tetrax=np.array([0,0.25,0,0.25,0,0.25,0.25,0,0])*2
tetray=np.array([0,0.25,0.25,0,0,0,0.25,0,0.25])*2
tetraz=np.array([0,0,0.25,0.25,0,0.25,0,0,0.25])*2
N_i=3
N_j=3
N_k=3
ones=2*np.linspace(0,max(max(N_i,N_j),N_k))
zeros=np.zeros(len(ones))

fig=plt.figure(figsize=(7,11))
ax=fig.gca(projection='3d')

for i in range(N_i):
    for j in range(N_j):
        for k in range(N_k):

            ax.plot(i*xi[0]+j*xj[0]+k*xk[0]+tetrax,
                       i*xi[1]+j*xj[1]+k*xk[1]+tetray,
                       i*xi[2]+j*xj[2]+k*xk[2]+tetraz,
                       "r.-",linewidth=1)#,color="r")
                       
            ######## PBC in x #########
            ax.plot((i+N_i)*xi[0]+j*xj[0]+k*xk[0]+tetrax,
                       (i+N_i)*xi[1]+j*xj[1]+k*xk[1]+tetray,
                       (i+N_i)*xi[2]+j*xj[2]+k*xk[2]+tetraz,"b.-",linewidth=1)

#            ax.plot((i-N_i)*xi[0]+j*xj[0]+k*xk[0]+tetrax,
#                    (i-N_i)*xi[1]+j*xj[1]+k*xk[1]+tetray,
#                    (i-N_i)*xi[2]+j*xj[2]+k*xk[2]+tetraz,"b-",linewidth=1)

            ######### PBC in y #########
            ax.plot(i*xi[0]+(j+N_j)*xj[0]+k*xk[0]+tetrax,
                       i*xi[1]+(j+N_j)*xj[1]+k*xk[1]+tetray,
                       i*xi[2]+(j+N_j)*xj[2]+k*xk[2]+tetraz,
                        "g.-",linewidth=1)

#            ax.plot(i*xi[0]+(j-N_j)*xj[0]+k*xk[0]+tetrax,
#                    i*xi[1]+(j-N_j)*xj[1]+k*xk[1]+tetray,
#                    i*xi[2]+(j-N_j)*xj[2]+k*xk[2]+tetraz,"g-",linewidth=1)

            ######## PBC in z #########
            ax.plot(i*xi[0]+(j)*xj[0]+(k+N_k)*xk[0]+tetrax,
                       i*xi[1]+(j)*xj[1]+(k+N_k)*xk[1]+tetray,
                       i*xi[2]+(j)*xj[2]+(k+N_k)*xk[2]+tetraz,
                        "c.-",linewidth=1)

#            ax.scatter(i*xi[0]+(j)*xj[0]+(k-N_k)*xk[0],
#                       i*xi[1]+(j)*xj[1]+(k-N_k)*xk[1],
#                       i*xi[2]+(j)*xj[2]+(k-N_k)*xk[2],color="c",s=10)
#


ax.plot(ones,ones,zeros,"b",label="X")
ax.plot(zeros,ones,ones,"g",label="Y")
ax.plot(ones,zeros,ones,"c",label="Z")
plt.legend()

plt.show()

fig=plt.figure(figsize=(7,11))
ax=fig.gca(projection='3d')


for i in range(N_i):
    for j in range(N_j):
        for k in range(N_k):
            
            ax.plot(i*xi[0]+j*xj[0]+k*xk[0]+tetrax,
                    i*xi[1]+j*xj[1]+k*xk[1]+tetray,
                    i*xi[2]+j*xj[2]+k*xk[2]+tetraz,
                    "r.-",linewidth=1)#,color="r")


indexi=1
indexj=1
indexk=1

hexagon1=np.array([r0+indexi*xi+indexj*xj+indexk*xk,
                   r2+indexi*xi+indexj*xj+indexk*xk,
                   
                   r1+(indexi-1)*xi+(indexj)*xj+(indexk+1)*xk,
                   r0+(indexi-1)*xi+(indexj)*xj+(indexk+1)*xk,
                   
                   r2+(indexi-1)*xi+(indexj)*xj+(indexk)*xk,
                   r1+(indexi-1)*xi+(indexj)*xj+(indexk)*xk,
                   r0+indexi*xi+indexj*xj+indexk*xk])

ax.plot(hexagon1[:,0],hexagon1[:,1],hexagon1[:,2],"k",linewidth=2,label="Hexagon1")

indexi=2
indexj=1
indexk=1


hexagon2=np.array([r0+indexi*xi+indexj*xj+indexk*xk,
                   r3+indexi*xi+indexj*xj+indexk*xk,
                   
                   r1+(indexi-1)*xi+(indexj+1)*xj+(indexk)*xk,
                   r0+(indexi-1)*xi+(indexj+1)*xj+(indexk)*xk,
                   
                   r3+(indexi-1)*xi+indexj*xj+indexk*xk,
                   r1+(indexi-1)*xi+indexj*xj+indexk*xk,
                   r0+indexi*xi+indexj*xj+indexk*xk])


ax.plot(hexagon2[:,0],hexagon2[:,1],hexagon2[:,2],"k--",linewidth=2,label="Hexagon2")

indexi=1
indexj=0
indexk=0


hexagon3=np.array([r2+indexi*xi+indexj*xj+indexk*xk,
                   r3+indexi*xi+indexj*xj+indexk*xk,
                   r1+(indexi-1)*xi+(indexj+1)*xj+(indexk)*xk,
                   r2+(indexi-1)*xi+(indexj+1)*xj+(indexk)*xk,
                   r3+(indexi-1)*xi+(indexj)*xj+(indexk+1)*xk,
                   r1+(indexi-1)*xi+(indexj)*xj+(indexk+1)*xk,
                   r2+indexi*xi+indexj*xj+indexk*xk,])


ax.plot(hexagon3[:,0],hexagon3[:,1],hexagon3[:,2],"k^-",linewidth=2,label="Hexagon3")

indexi=2
indexj=0
indexk=0

hexagon4=np.array([r2+indexi*xi+indexj*xj+indexk*xk,
                   r3+indexi*xi+indexj*xj+indexk*xk,
                   r0+(indexi)*xi+(indexj+1)*xj+(indexk)*xk,
                   r2+(indexi)*xi+(indexj+1)*xj+(indexk)*xk,
                   r3+(indexi)*xi+(indexj)*xj+(indexk+1)*xk,
                   r0+(indexi)*xi+(indexj)*xj+(indexk+1)*xk,
                   r2+indexi*xi+indexj*xj+indexk*xk,])

ax.plot(hexagon4[:,0],hexagon4[:,1],hexagon4[:,2],"ko-",linewidth=2,label="Hexagon4")

plt.legend()

plt.show()

