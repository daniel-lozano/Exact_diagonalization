import numpy as np
import matplotlib.pyplot as plt
from constants import *
from CSW_functions import *

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np



h_list=[]
k_list=[]
l_list=[]

n_points=100

x=np.linspace(0,1,n_points)
fixed=np.ones(n_points)
n_points_1=0

##(000) -> (020) ok

h_list.extend(0*np.linspace(0,1,2*n_points))
k_list.extend(2*np.linspace(0,1,2*n_points))
l_list.extend(0*np.linspace(0,1,2*n_points))

##(020) -> (120) ok
h_list.extend(x)
k_list.extend(2*fixed)
l_list.extend(0*fixed)

## (120) -> (111) ok
h_list.extend(1*fixed)
k_list.extend(2*fixed-x)
l_list.extend(x)

## (111) --> (000)
h_list.extend(-x[::-1]+fixed)
k_list.extend(-x[::-1]+fixed)
l_list.extend(-x[::-1]+fixed)


##(000) --> (020)
h_list.extend(0*fixed)
k_list.extend(2*x)
l_list.extend(0*fixed)

##(020)--> (1/2,2,1/2)
h_list.extend(0.5*x)
k_list.extend(2*fixed)
l_list.extend(0.5*x)

##(020)--> (1/2,2,1/2)
h_list.extend(0.5*x)
k_list.extend(2*fixed)
l_list.extend(0.5*x)

##(1/2,2,1/2) --> (111)
h_list.extend(0.5*x+0.5*fixed)
k_list.extend(2*fixed-x)
l_list.extend(0.5*x+0.5*fixed)

##(111)-->(3/2,3/2,0)
h_list.extend(0.5*x+fixed)
k_list.extend(0.5*x+fixed)
l_list.extend(fixed-x)

##(3/2,3/2,0)--> (0,0,0)
h_list.extend(-1.5*x+1.5*fixed)
k_list.extend(-1.5*x+1.5*fixed)
l_list.extend(fixed*0)

##(0,0,0)-->(3/2,3/2,0)
h_list.extend(1.5*x)
k_list.extend(1.5*x)
l_list.extend(fixed*0)


##(3/2,3/2,0)-->(1,2,0)
h_list.extend(1.5*fixed-0.5*x)
k_list.extend(0.5*x+1.5*fixed)
l_list.extend(fixed*0)

##(1,2,0)-->(1/2,2,1/2)
h_list.extend(1*fixed-0.5*x)
k_list.extend(2*fixed)
l_list.extend(0.5*x)

fig=plt.figure(figsize=(7,8))
ax=fig.gca(projection='3d')
ax.plot(h_list,k_list,l_list)


Shift=0.1
xs = (0, 0, 0.5, 1, 3/2., 1)
ys = (0, 2, 2, 2, 3./2., 1)
zs = (0+Shift, 0+Shift, 0.5+Shift, 0+Shift, 0+Shift, 1+Shift)
Labels=[" $\Gamma$ "," X ", "U" ,"W","K","L"]


for  x, y, z, text in zip(xs, ys, zs,Labels):
    label = text #+" (%0.1f,%0.1f,%0.1f)" %(x,y,z-Shift)
    ax.text(x, y, z, label, None,fontsize=20)


ax.set_xlabel("$ (h00) $",fontsize=20)
ax.set_ylabel("$ (0k0) $",fontsize=20)
ax.set_zlabel("$ (00l) $",fontsize=20)
ax.set_xticks((0,0.5,1,1.5,2))
ax.set_yticks((0,0.5,1,1.5,2))
ax.set_zticks((0,0.5,1,1.5,2))
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_zlim(0,2)
plt.show()
