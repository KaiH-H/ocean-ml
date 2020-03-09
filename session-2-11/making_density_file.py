from netCDF4 import Dataset
import numpy as np
import seawater as sw

<<<<<<< HEAD
dataset = Dataset(r'/Users/brownscholar/Desktop/Internships/dataset-armor-3d-rep-weekly_1574699840388.nc')

=======
dataset = Dataset(r'/Users/helenfellow/Documents/cnn_paper/data/dataset-armor-3d-rep-weekly_1574699840388.nc')
>>>>>>> ae2a66d07524f15dcce27fbe52b54d85ec246ec5
# first step: import the data and get temp, salinity pressure
temperature = dataset['to']
salinity = dataset['so']
pressure = dataset['depth']

print(temperature.shape)
print(salinity.shape)
print(pressure.shape)

<<<<<<< HEAD
#print(pressure[:])
#second step: make the pressure data 3 dimenional

pressure_3d = np.zeros((31,80,27)) # 

first_layer = np.repeat(10, 80*27).reshape(80,27)

second_layer = np.repeat(20, 80*27).reshape(80,27)

# for depth_level in pressure[:]:
# 	layer = np.repeat(depth_level, 80*27).reshape(80,27) # 2D array

for i in range(0,31):
	pressure_3d[i,:,:] = np.repeat(pressure[i], 80*27).reshape(80,27)


density = sw.dens(salinity[:],temperature[:],pressure_3d)

density = density -1000

print(density.shape)

	

for i in range(0,1356):
	my_file = open("density_"+str(i)+".txt","w")
	for j in range(0,31):
		for k in range(0,80):
			for w in range(0,27):
				my_file.write(str(density[i,j,k,w]))
				my_file.write("\n")
	my_file.close()

# to do: 

# inputs: salinity, temperature, pressure in form of netcdf file
=======
print(pressure[:])
#second step: make the pressure data 3 dimenional


pressure_3d = np.zeros((31,80,27))

# first_layer = np.repeat(10,80*27).reshape(80,27)

# second_layer = np.repeat(20,80*27).reshape(80,27)

 # for depth_level in pressure[:]:
 # 	print(np.repeat(depth_level,80*27).reshape((80,27)))
#print(pressure[:])
for i in range(0,31):
	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))

#salinity = float(salinity)
#temperature = float(temperature)

density = sw.dens(salinity[:],temperature[:],pressure_3d)

print(density)
# to do: 

# inputs: salinity, temperature, pressure in form of netcdf file

>>>>>>> ae2a66d07524f15dcce27fbe52b54d85ec246ec5
