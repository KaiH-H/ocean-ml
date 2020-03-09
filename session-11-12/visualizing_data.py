from netCDF4 import Dataset
import numpy.ma as ma
<<<<<<< HEAD
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from datetime import timedelta
from datetime import date
=======
from datetime import date
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

>>>>>>> ae2a66d07524f15dcce27fbe52b54d85ec246ec5

# import the netcdf file using Dataset
dataset = Dataset(r'/Users/brownscholar/Desktop/Internships/ocean-ml/session-10-31/ssh_1572470095877.nc')

# read in and create variable for lat:
lat = dataset['latitude']

# lon:
lon = dataset['longitude']


# adt:
adt = dataset['adt']

# start_date = date(1950,1,1)
# delta = timedelta(days = int(time[0]))
# observation_date = (start_date+delta).strftime("%m/%d/%Y")

# you will need this:
BATS_lat_max = 39.453
BATS_lon_max = 360 -59.648999999999994 # converting from degrees west to degrees east
BATS_lat_min = 19.663 
BATS_lon_min = 360 -66.211 #same

# print(lat[:])

lat_index = set()
index = 0

for i in lat: 
	if i >= BATS_lat_min and i <= BATS_lat_max:
		lat_index.add(index) # Must do .add in order to add for a set
	index += 1

# print(lat_index)     

lon_index = set()
index2 = 0

for i in lon: 
	if i >= BATS_lon_min and i <= BATS_lon_max:
		lon_index.add(index2) # Must do .add in order to add for a set
	index2 += 1     

# print(lon_index)     

lat_index_min = min(lat_index)
lat_index_max = max(lat_index)

lon_index_min = min(lon_index)
lon_index_max = max(lon_index)

print(lat_index_min)
print(lat_index_max)
print(lon_index_min)
print(lon)

BATSadt = adt[:, lat_index_min:lat_index_max, lon_index_min:lon_index_max]

# creating colorbar scale:
high = ma.amax(adt)
low = ma.amin(adt)
colorbar_scale =["%.2E"%low]
i = 0.16
while i<1:
	value = (high-low)*i
	colorbar_scale.append("%.2E"%value)
	i+=0.16
## ^^ ignore this but when you make your colorbar you can add the 
## scale by: cbar.ax.set_yticklabels(colorbar_scale)



# write code for global ocean here: 
adt_2d = adt[0,:,:]
plt.imshow(adt_2d,origin='lower')
plt.title("Sea Surface Height - Global Ocean (01/01/1993)")

plt.ylabel("Latitude")
plt.xlabel("Longitude")

cbar = plt.colorbar()
cbar.set_label("Sea Surface Height (m)")
cbar.ax.set_yticklabels(colorbar_scale)

x1,y1 = [lon_index_min,lon_index_max],[lat_index_min,lat_index_min] # Bottom horizontal line
x2,y2 = [lon_index_min,lon_index_min],[lat_index_max,lat_index_min] # Left vertical
x3,y3 = [lon_index_min,lon_index_max],[lat_index_max,lat_index_max] # Top horizontal
x4,y4 = [lon_index_max,lon_index_max],[lat_index_max,lat_index_min] # Right vertical

plt.plot(x1,y1,x2,y2,x3,y3,x4,y4, color = 'r', linewidth = 1)

red_line = mlines.Line2D([], [], color='r',
                          markersize=15, label='BATS region',linewidth = 1)
plt.legend(handles=[red_line])

plt.xticks(ma.arange(0,1440,200),lon[0::200]) #start:stop:step --> No stop (stop is the end) 
plt.yticks(ma.arange(0,720,100),lat[0::100]) # becomes start::step

plt.show()

# write code for BATS part here:


# print(BATSadt.shape)
