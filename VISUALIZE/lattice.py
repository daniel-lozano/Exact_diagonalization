import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


xi=np.array([1,1,0])
xj=np.array([0,1,1])
xk=np.array([1,0,1])

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

            ax.scatter(i*xi[0]+j*xj[0]+k*xk[0],
                       i*xi[1]+j*xj[1]+k*xk[1],
                       i*xi[2]+j*xj[2]+k*xk[2],color="r")

            ax.scatter((i+N_i)*xi[0]+j*xj[0]+k*xk[0],
                       (i+N_i)*xi[1]+j*xj[1]+k*xk[1],
                       (i+N_i)*xi[2]+j*xj[2]+k*xk[2],color="b",s=10)
            ax.scatter((i-N_i)*xi[0]+j*xj[0]+k*xk[0],
                       (i-N_i)*xi[1]+j*xj[1]+k*xk[1],
                       (i-N_i)*xi[2]+j*xj[2]+k*xk[2],color="b",s=10)

            ax.scatter(i*xi[0]+(j+N_j)*xj[0]+k*xk[0],
                       i*xi[1]+(j+N_j)*xj[1]+k*xk[1],
                       i*xi[2]+(j+N_j)*xj[2]+k*xk[2],color="g",s=10)
            ax.scatter(i*xi[0]+(j-N_j)*xj[0]+k*xk[0],
                       i*xi[1]+(j-N_j)*xj[1]+k*xk[1],
                       i*xi[2]+(j-N_j)*xj[2]+k*xk[2],color="g",s=10)

            ax.scatter(i*xi[0]+(j)*xj[0]+(k+N_k)*xk[0],
                       i*xi[1]+(j)*xj[1]+(k+N_k)*xk[1],
                       i*xi[2]+(j)*xj[2]+(k+N_k)*xk[2],color="c",s=10)
            ax.scatter(i*xi[0]+(j)*xj[0]+(k-N_k)*xk[0],
                       i*xi[1]+(j)*xj[1]+(k-N_k)*xk[1],
                       i*xi[2]+(j)*xj[2]+(k-N_k)*xk[2],color="c",s=10)



ax.plot(ones,ones,zeros,"b",label="X")
ax.plot(zeros,ones,ones,"c",label="Y")
ax.plot(ones,zeros,ones,"g",label="Z")
plt.legend()
plt.show()


