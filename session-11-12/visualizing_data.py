from netCDF4 import Dataset
import numpy.ma as ma

# import the netcdf file using Dataset
dataset = Dataset(r'/Users/helenfellow/Documents/InternGit/ocean-ml/session-10-31/ssh_1572470095877.nc')

# read in and create variable for lat:
lat = dataset['latitude']

# lon:
lon = dataset['longitude']

# adt:
adt = dataset['adt']

# you will need this:
BATS_lat_max = 39.453
BATS_lon_max = 360 -59.648999999999994 # converting from degrees west to degrees east
BATS_lat_min = 19.663 
BATS_lon_min = 360 -66.211 #same

print(lat[:])

lat_index = set()
index = 0

for i in lat: 
	if i >= BATS_lat_min and i <= BATS_lat_max:
		lat_index.add(index) # Must do .add in order to add for a set
	index += 1

print(lat_index)     

lon_index = set()
index2 = 0

for i in lon: 
	if i >= BATS_lon_min and i <= BATS_lon_max:
		lon_index.add(index2) # Must do .add in order to add for a set
	index2 += 1     

print(lon_index)     

lat_index_min = min(lat_index)
lat_index_max = max(lat_index)

lon_index_min = min(lon_index)
lon_index_max = max(lon_index)

print("Max of Lat:", str(lat_index_max), "\nMin of Lat:", str(lat_index_min), "\nMax of Lon:", lon_index_max, "\nMin of Lon:", lon_index_min)

BATSadt = adt[:, lat_index_min:lat_index_max, lon_index_min:lon_index_max]

print(BATSadt.shape)
