from netCDF4 import Dataset
import numpy as np
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/Internships/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset['depth']
temperture = dataset['to']
salinity = dataset['so']

# print(pressure.shape)
# print(temperture.shape)
# print(salinity.shape)

pressure_3d = np.zeros((31,80,27))

# for depth_level in pressure:
# 	print(np.repeat(depth_level,80*27).reshape((80,27)))


for i in range(0,31):
	#print(np.repeat(pressure[i],80*27).reshape((80,27)))
	pressure_3d[:] = np.repeat(pressure[:],80*27).reshape((80,27))
	#print(pressure_3d[i,:,:])

density = sw.dens(salinity[:],temperture[:],pressure_3d)
density = density-1000

print(density.shape)

num = 0


for i in range(0,1326):
	data = open('datafile_' + str(num), 'w')
	num += 1
	for nl in range(0,31):
		for nf in range(0,80):
			for nc in range(0,27):
				data.write(density[i, nl, nf, nc])
	data.close()




	#nl, nf, nc
	# depth, latitude, longitude

