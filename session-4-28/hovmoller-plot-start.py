from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

omega = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')

w = omega['w']
lat = omega['latitude']
depth = omega['depth']
longitude = omega['lon']

print(w.shape)

array1 = w[:,0,:,0]
array2 = w[:,0,:,1]
array3 = w[:,0,:,2]

top = cm.get_cmap('Blues_r')
bottom = cm.get_cmap('Reds')
newcolors = np.vstack((top(np.linspace(0, 1, 10)),
                       bottom(np.linspace(0, 1, 10))))
RedBlue = ListedColormap(newcolors, name='RedBlue')

fig, ax = plt.subplots(3,1)
print(fig, ax)

array1_flip = np.swapaxes(array1,0,1)
array2_flip = np.swapaxes(array2,0,1)
array3_flip = np.swapaxes(array3,0,1)

ax[0].pcolormesh(array1_flip,cmap=RedBlue, vmax = 10, vmin = -10)
ax[0].set_title("Depth = " + str(depth[0]))
ax[1].pcolormesh(array2_flip,cmap=RedBlue, vmax = 10, vmin = -10)
ax[1].set_title("Depth = " + str(depth[1]))
ax[2].pcolormesh(array3_flip,cmap=RedBlue, vmax = 10, vmin = -10)
ax[2].set_title("Depth = " + str(depth[2]))

fig.suptitle("Hovmoller Diagram at Latitude " + str(lat[0]))
plt.show()




