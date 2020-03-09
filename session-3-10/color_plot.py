import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

w_file = open('/Users/brownscholar/Desktop/Internships/ocean-ml/session-3-10/ss1/ss1a2ww.gr',"r") #fix this
#original_data = #open netcdf file

#get latitude and longitude from netcdf file: 
# here:


num_lat = 80
num_lon = 27
levels = 30

# make empty numpy array of lat, lon depth shape for storing w:
w_array = np.zeros((num_lat,num_lon,levels))

# use a loop to read w_file into the variable 
#(skip first two lines of the file)

w_file.readline()
w_file.readline()

for i in range(0,levels):
	for j in range(0, num_lon):
		for k in range(0,num_lat):
			temp = w_file.readline()
			w_array[k,j,i] = temp


#this stuff defines the colorspace (we can google colormaps to learn more if we want to)
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')

plt.pcolormesh(w_array[2:78,2:25,0], cmap = newcmp)

plt.show()

#now select one level of the data (surface level):



#and use the following function to plot your data:
#function to make colorplot is:
# p = plt.pcolormesh(V,cmap = newcmp), where V is the numpy array with the data
