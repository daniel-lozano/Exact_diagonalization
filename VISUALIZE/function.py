import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as mp3d
import numpy as np

#### Up tetrahedra
#Tx1 = [[0,0,0],
#        [0,1,1],
#        [1,0,1]]
#
#Tx2 = [[1,1,0],
#        [0,1,1],
#        [1,0,1]]
#
#Tx3 = [[0,0,0],
#        [1,1,0],
#        [1,0,1]]
#
#Tx4 = [[0,0,0],
#        [1,1,0],
#        [0,1,1]]
#### Down tetrahedra
#Dx1 = [[0,0,1],
#        [1,1,1],
#        [1,0,0]]
#
#Dx2 = [[1,1,1],
#        [0,1,0],
#        [1,0,0]]
#
#Dx3 = [[0,0,1],
#        [1,1,1],
#        [1,0,0]]
#
#Dx4 = [[0,0,1],
#        [1,1,1],
#        [0,1,0]]
#shift_vec_1=[-1,+1,1]
#Shift_1=np.array([shift_vec_1,shift_vec_1,shift_vec_1])
#shift_vec_2=[1,-1,1]
#Shift_2=np.array([shift_vec_2,shift_vec_2,shift_vec_2])
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#up1 = mp3d.art3d.Poly3DCollection([Tx1], alpha=0.5, linewidth=1)
#up2 = mp3d.art3d.Poly3DCollection([Tx2], alpha=0.5, linewidth=1)
#up3 = mp3d.art3d.Poly3DCollection([Tx3], alpha=0.5, linewidth=1)
#up4 = mp3d.art3d.Poly3DCollection([Tx4], alpha=0.5, linewidth=1)
#
#down1 = mp3d.art3d.Poly3DCollection([Dx1+Shift_1], alpha=0.5, linewidth=1)
#down2 = mp3d.art3d.Poly3DCollection([Dx2+Shift_1], alpha=0.5, linewidth=1)
#down3 = mp3d.art3d.Poly3DCollection([Dx3+Shift_1], alpha=0.5, linewidth=1)
#down4 = mp3d.art3d.Poly3DCollection([Dx4+Shift_1], alpha=0.5, linewidth=1)
#
#down5 = mp3d.art3d.Poly3DCollection([Dx1+Shift_2], alpha=0.5, linewidth=1)
#down6 = mp3d.art3d.Poly3DCollection([Dx2+Shift_2], alpha=0.5, linewidth=1)
#down7 = mp3d.art3d.Poly3DCollection([Dx3+Shift_2], alpha=0.5, linewidth=1)
#down8 = mp3d.art3d.Poly3DCollection([Dx4+Shift_2], alpha=0.5, linewidth=1)
#
#
#
#alpha = 0.5
#up1.set_facecolor((0, 0, 1, alpha))
#up2.set_facecolor((0, 0, 1, alpha))
#up3.set_facecolor((0, 0, 1, alpha))
#up4.set_facecolor((0, 0, 1, alpha))
#
#down1.set_facecolor((0, 0, 1, alpha))
#down2.set_facecolor((0, 0, 1, alpha))
#down3.set_facecolor((0, 0, 1, alpha))
#down4.set_facecolor((0, 0, 1, alpha))
#
#down5.set_facecolor((0, 0, 1, alpha))
#down6.set_facecolor((0, 0, 1, alpha))
#down7.set_facecolor((0, 0, 1, alpha))
#down8.set_facecolor((0, 0, 1, alpha))
#
#ax.add_collection3d(up1)
#ax.add_collection3d(up2)
#ax.add_collection3d(up3)
#ax.add_collection3d(up4)
#
#ax.add_collection3d(down1)
#ax.add_collection3d(down2)
#ax.add_collection3d(down3)
#ax.add_collection3d(down4)
#ax.add_collection3d(down5)
#ax.add_collection3d(down6)
#ax.add_collection3d(down7)
#ax.add_collection3d(down8)
#ax.set_xlim(0,2)
#ax.set_ylim(0,2)
#ax.set_zlim(0,2)
#
#
#plt.show()

def plot_solid_tetrahedra(ax,translation):
    ### Up tetrahedra
    Tx1 = [[0,0,0],
            [0,1,1],
            [1,0,1]]

    Tx2 = [[1,1,0],
            [0,1,1],
            [1,0,1]]
            
    Tx3 = [[0,0,0],
            [1,1,0],
            [1,0,1]]
            
    Tx4 = [[0,0,0],
            [1,1,0],
            [0,1,1]]
    ### Down tetrahedra
    Dx1 = [[0,0,1],
            [1,1,1],
            [1,0,0]]

    Dx2 = [[1,1,1],
            [0,1,0],
            [1,0,0]]

    Dx3 = [[0,0,1],
            [1,1,1],
            [1,0,0]]

    Dx4 = [[0,0,1],
            [1,1,1],
            [0,1,0]]
    shift_vec_1=[-1,+1,1]
    Shift_1=np.array([shift_vec_1,shift_vec_1,shift_vec_1])
    shift_vec_2=[1,-1,1]
    Shift_2=np.array([shift_vec_2,shift_vec_2,shift_vec_2])
    
    FCC_translation=np.array([translation,translation,translation])

#    fig = plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
    up1 = mp3d.art3d.Poly3DCollection([Tx1+FCC_translation], alpha=0.5, linewidth=1)
    up2 = mp3d.art3d.Poly3DCollection([Tx2+FCC_translation], alpha=0.5, linewidth=1)
    up3 = mp3d.art3d.Poly3DCollection([Tx3+FCC_translation], alpha=0.5, linewidth=1)
    up4 = mp3d.art3d.Poly3DCollection([Tx4+FCC_translation], alpha=0.5, linewidth=1)

    down1 = mp3d.art3d.Poly3DCollection([Dx1+Shift_1+FCC_translation], alpha=0.5, linewidth=1)
    down2 = mp3d.art3d.Poly3DCollection([Dx2+Shift_1+FCC_translation], alpha=0.5, linewidth=1)
    down3 = mp3d.art3d.Poly3DCollection([Dx3+Shift_1+FCC_translation], alpha=0.5, linewidth=1)
    down4 = mp3d.art3d.Poly3DCollection([Dx4+Shift_1+FCC_translation], alpha=0.5, linewidth=1)

    down5 = mp3d.art3d.Poly3DCollection([Dx1+Shift_2+FCC_translation], alpha=0.5, linewidth=1)
    down6 = mp3d.art3d.Poly3DCollection([Dx2+Shift_2+FCC_translation], alpha=0.5, linewidth=1)
    down7 = mp3d.art3d.Poly3DCollection([Dx3+Shift_2+FCC_translation], alpha=0.5, linewidth=1)
    down8 = mp3d.art3d.Poly3DCollection([Dx4+Shift_2+FCC_translation], alpha=0.5, linewidth=1)



    alpha = 0.2
    up1.set_facecolor((0, 0, 1, alpha))
    up2.set_facecolor((0, 0, 1, alpha))
    up3.set_facecolor((0, 0, 1, alpha))
    up4.set_facecolor((0, 0, 1, alpha))

    down1.set_facecolor((0.5, 0, 0, alpha))
    down2.set_facecolor((0.5, 0, 0, alpha))
    down3.set_facecolor((0.5, 0, 0, alpha))
    down4.set_facecolor((0.5, 0, 0, alpha))

    down5.set_facecolor((0.5, 0, 0, alpha))
    down6.set_facecolor((0.5, 0, 0, alpha))
    down7.set_facecolor((0.5, 0, 0, alpha))
    down8.set_facecolor((0.5, 0, 0, alpha))
    
    ax.add_collection3d(up1)
    ax.add_collection3d(up2)
    ax.add_collection3d(up3)
    ax.add_collection3d(up4)

    ax.add_collection3d(down1)
    ax.add_collection3d(down2)
    ax.add_collection3d(down3)
    ax.add_collection3d(down4)
    ax.add_collection3d(down5)
    ax.add_collection3d(down6)
    ax.add_collection3d(down7)
    ax.add_collection3d(down8)
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)
    ax.set_zlim(0,2)
    
