import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

### Tetrahedra positions ###

x=np.array([0,1,0,0,1,1,1,0,1])
y=np.array([0,1,1,0,0,1,0,1,0])
z=np.array([0,0,1,0,1,0,1,1,1])

x_i=np.array([2,2,1,2,1,2,1,1,1])
y_i=np.array([-1,0,-1,-1,0,0,0,-1,-1])
z_i=np.array([1,2,2,1,1,2,1,2,2])

translation_x=np.ones(len(x))
translation_y=np.ones(len(y))
translation_z=np.ones(len(z))

###########################################################################
############################### Lattice ##############################
###########################################################################

x_direction=np.array([1,1,-1,-1])
y_direction=np.array([1,1,1,1])
z_direction=np.array([1,-1,-1,1])

x_pos=np.array([0,1,1,0])
y_pos=np.array([0,1,0,1])
z_pos=np.array([0,0,1,1])
move=np.ones(len(x_pos))


fig=plt.figure()
ax=fig.gca(projection='3d')
Ni=int(input("Number of tetrahedra in the x direction="))
Nj=int(input("Number of tetrahedra in the y direction="))
Nk=int(input("Number of tetrahedra in the z direction="))

points=10
x_line=np.linspace(0,Ni*2,points)
zeros=np.zeros(len(x_line))
ones=np.ones(len(x_line))
y_line=np.linspace(0,Nj*2,points)
z_line=np.linspace(0,Nk*2,points)


for i in range(Ni):
    for j in range(Nj):
        for k in range(Nk):
#            X=x+2*i+2*k
#            Y=y+2*k
#            Z=z+2*j+2*k
            X=x+translation_x*2*i
            Y=y+translation_y*2*j
            Z=z+translation_z*2*k
            
            X_I=x_i+translation_x*2*i
            Y_I=y_i+translation_y*2*j
            Z_I=z_i+translation_z*2*k
            ### Spins being added ###
            ax.quiver(x_pos+move*2*i,y_pos+move*2*j,z_pos+move*2*k,x_direction,y_direction,z_direction,length=0.2,color="red")
            ### Position of tetrahedra ###
            ax.plot(X,Y,Z,color="gray",marker="o")

            ax.plot(X_I,Y_I,Z_I,color="k",marker="o")

#            ax.plot(X+1,Y,Z+1,color="g",marker="o")
#
            ax.plot(x_line+2*i,x_line+2*j,zeros+2*k,"--",color="lime",alpha=0.4)
            ax.plot(x_line-2*i,x_line+2*j,zeros+2*k,"--",color="lime",alpha=0.4)
            
            ax.plot(x_line+2*i,-x_line+ones+2*(j+1),ones+2*k,"c--",alpha=0.5)
            ax.plot(x_line+2*i,-x_line+ones+2*(j-1),ones+2*k,"c--",alpha=0.5)


ax.plot(x_line,y_line,z_line,"gold",linewidth=2)

N_max=max(max(Ni,Nj),Nk)
ax.set_title("%dX%dX%d Pyrochlore" %(Ni,Nj,Nk))
ax.set_xlim(0,2*N_max)
ax.set_ylim(0,2*N_max)
ax.set_zlim(0,2*N_max)
ax.set_xlabel("$ x $",size=20)
ax.set_ylabel("$ y $",size=20)
ax.set_zlabel("$ z $",size=20)
plt.show()






