import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x=np.linspace(-2.5,2.5,100)

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


