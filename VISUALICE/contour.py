import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x=np.linspace(-2.5,2.5,100)

hh,l= np.meshgrid(x, x)
Z1=np.cos(np.pi*(l+hh))+np.cos(np.pi*(l-hh))
Z2=np.cos(np.pi*(l+hh))+np.cos(np.pi*(l-hh))+np.cos(2*np.pi*hh)

cmap_label="inferno"

plt.subplot(131)
plt.imshow(Z1,cmap=cmap_label,extent=[-2.5,2.5,-2.5,2.5])
plt.xlabel("hh")
plt.ylabel("l")
plt.title("J2")
plt.subplot(132)
plt.imshow(Z2,cmap=cmap_label,extent=[-2.5,2.5,-2.5,2.5])
plt.xlabel("hh")
plt.ylabel("l")
plt.title("J3")
plt.subplot(133)
plt.imshow(Z2+Z1,cmap=cmap_label,extent=[-2.5,2.5,-2.5,2.5])
plt.xlabel("hh")
plt.ylabel("l")
plt.title("J3+J2")
plt.show()


