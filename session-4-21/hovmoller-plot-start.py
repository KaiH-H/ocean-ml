from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

omega = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')

w = omega['w']
lat = omega['latitude']

print(w.shape)

array = w[:,0,:,0]

top = cm.get_cmap('Blues_r')
bottom = cm.get_cmap('Reds')
newcolors = np.vstack((top(np.linspace(0, 1, 10)),
                       bottom(np.linspace(0, 1, 10))))
RedBlue = ListedColormap(newcolors, name='RedBlue')

array_flip = np.swapaxes(array,0,1)
print(array_flip.shape)

plt.pcolormesh(array_flip,cmap=RedBlue)

plt.title("Hovmoller Diagram at Latitude " + str(lat[0]))
plt.show()




