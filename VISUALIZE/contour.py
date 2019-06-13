import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import animatplot as amp

x=np.linspace(-2.5,2.5,500)

hh,l= np.meshgrid(x, x)

AT2=1.
AT3=1
BT3=1.
CT3=1.

Z_J2=(2*AT2)*(np.cos(np.pi*(l+hh))+np.cos(np.pi*(l-hh)))
Z_J3=2*(AT3+BT3)*(np.cos(np.pi*(l+hh))+np.cos(np.pi*(l-hh)))+2*CT3*np.cos(2*np.pi*hh)


cmap_label="inferno"

plt.subplot(121)
plt.imshow(Z_J2,cmap=cmap_label,extent=[-2.5,2.5,-2.5,2.5])
plt.xlabel("$ (hh0) $")
plt.ylabel("$ (00l) $")
plt.title("$ J_2 $")
plt.subplot(122)
plt.imshow(Z_J3,cmap=cmap_label,extent=[-2.5,2.5,-2.5,2.5])
plt.xlabel("$ (hh0) $")
plt.ylabel("$ (00l) $")
plt.title("$ J_{3a} $  and  $ J_{3b} $ ")
plt.show()

bt=np.linspace(0,2,100)
hh,l,BT= np.meshgrid(x, x, bt)
cmap_label="jet"


def Z_J3(hh,l,BT3):
    return 2*(1+BT3)*(np.cos(np.pi*(l+hh))+np.cos(np.pi*(l-hh)))+2*BT3*np.cos(2*np.pi*hh)

pcolormesh_data =Z_J3(hh,l,BT)
pcolormesh_block = amp.blocks.Pcolormesh(hh[:,:,0], l[:,:,0], pcolormesh_data,
                                         t_axis=2, vmin=-1, vmax=1,cmap=cmap_label)
plt.colorbar(pcolormesh_block.quad)
plt.xlabel("$ (hh0) $")
plt.ylabel("$ (00l) $")
timeline = amp.Timeline(bt, fps=10)

# now to contruct the animation
anim = amp.Animation([pcolormesh_block], timeline)
anim.controls()

plt.show()

