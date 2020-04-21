import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from netCDF4 import Dataset
import numpy as np

# stuff that sets the plotting settings
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')
_min = -10
_max = 10
#

# facts about our data:
num_lat = 80
num_lon = 27
levels = 30
dates = 1356
z_step = 10 


# 1 - import netcdf file
file = Dataset('/Users/brownscholar/Desktop/fortran_files/omega.nc')

# 2 - load the w variable
w_var = file['w'][:]

# 3 - get lat x lon numpy array of w_variable (pick a single depth and a single time)
lat_lon1 = w_var[0,:,:,0]

#4 - plot the numpy array you have: 
plt.pcolormesh(lat_lon1, cmap = newcmp)
plt.colorbar(label = 'm/day')
plt.show()

# once you have this, you can use plt.pcolormesh() to plot it.
# ex: if your numpy array was called my_numpy_array:
# plt.pcolormesh(my_numpy_array,cmap = newcmp,vmin = _min, vmax = _max)
# to add colorbar: 
# plt.colorbar(label = 'm/day')
