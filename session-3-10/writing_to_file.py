from netCDF4 import Dataset
import numpy as np
import seawater as sw 
import datetime as td
import tricubic
from interpolate import interp

dataset = Dataset(r'/Users/brownscholar/Desktop/Internships/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset['depth']
temperture = dataset['to']
salinity = dataset['so']

pressure_interp = interp(temperture[0,:,:,:])
print("interpolated!!!")

# print(pressure.shape)
# print(temperture.shape)
# print(salinity.shape)

pressure_3d = np.zeros((31,80,27))

# for depth_level in pressure:
# 	print(np.repeat(depth_level,80*27).reshape((80,27)))


for i in range(0,31):
	#print(np.repeat(pressure[i],80*27).reshape((80,27)))
	pressure_3d[:] = np.repeat(pressure[i],80*27).reshape((80,27))
	#print(pressure_3d[i,:,:])

density = sw.dens(salinity[:],temperture[:],pressure_3d)
density = density-1000

print(density.shape)


time = dataset['time']

start_date = td.date(1950,1,1)


for i in range(0,1356):
	density_interp = interp(density[i,:,:,:])
	date_in_dataset = td.timedelta(hours =int(time[i]))
	day = date_in_dataset + start_date
	year_month_day = (day.strftime("%y") + day.strftime("%m") + day.strftime("%d"))
	data = open('/Users/brownscholar/Desktop/Internships/dates/datafile_' + year_month_day + '.gr', 'w')
	data.write("\t30\n27\t80\n")
	for nl in range(0,30):
		for nf in range(0,80):
			for nc in range(0,27):
				data.write(str(density_interp[nl, nf, nc]))
				data.write("\n")
	data.close()




	#nl, nf, nc
	# depth, latitude, longitude

