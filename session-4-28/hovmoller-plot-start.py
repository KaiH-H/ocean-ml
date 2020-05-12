from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import datetime as dt

omega = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')

w = omega['w']
lat = omega['latitude']
depth = omega['depth']
longitude = omega['longitude']
time = omega['time']

print(w.shape)
print(time.shape)

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

i = 0

start_date = dt.date(1950,1,1)
all_years = []

for i in time:
	hours = dt.timedelta(hours = int(i))
	year = (start_date + hours)
	i += 1
	all_years.append(year.year)

j = 0
for k in all_years:
	if k == 1993:
		j += 1
	else: 
		continue

# Repeats 52 times
print('j = ' + str(j))





ax[0].pcolormesh(array1_flip,cmap=RedBlue, vmax = 10, vmin = -10)
ax[0].set_title("Depth = " + str(depth[0]))
ax[0].set_yticks(np.arange(0,23,5))

ax[0].set_xticks(np.arange(0,27,3)) # note you still need this part for the spacing
ax[0].set_xticklabels(all_years[0::52])

ax[1].pcolormesh(array2_flip,cmap=RedBlue, vmax = 10, vmin = -10)
ax[1].set_title("Depth = " + str(depth[1]))
ax[1].set_yticks(np.arange(0,23,5))
ax[2].pcolormesh(array3_flip,cmap=RedBlue, vmax = 10, vmin = -10)
ax[2].set_title("Depth = " + str(depth[2]))
ax[2].set_yticks(np.arange(0,23,5))

fig.suptitle("Hovmoller Diagram at Latitude " + str(lat[0]))
plt.show()




