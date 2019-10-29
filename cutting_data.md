# Today we’re going to put a few things we’ve learned together and cut our data

Check out this beautiful beach in Bermuda: 
![bermuda :')](https://www.gotobermuda.com/sites/default/files/styles/hero/public/head-south-shore-horseshoe-bay-beach.jpg?itok=OBBhtfew)

# First a bit about our data: 
Review: We have been looking at sea_velocity_19930101.nc, which is one of many netcdf files downloaded from [here](http://marine.copernicus.eu.)This file contains the global horizontal and vertical velocities of the ocean, called ugos and vgos respectively.

We want to match that data to the data about carbon in the ocean
* This data comes from BIOS, which is the Bermuda Institute of Ocean Sciences.  
* The data we are interested in is called BATS, which stands for Bermuda Atlantic Time-series Study. 
* BATS has collected data on the physical, biological, and chemical properties of the ocean every month since before 1988. 
* BATS is **not** global, it covers  roughly this: 

<img src="https://raw.githubusercontent.com/madesai22/ocean-ml/master/images/BATS_data.png" width="400" height="450" />


Our goal for today: 
Given a netcdf file (sea_velocity_19930101.nc) with data fields ugos and vgos (horizontal and vertical velocities) for the whole globe (all latitudes and longitudes), we want to create variables BATS_ugos and BATS_vgos which contain just the ugos and vgos for the BATS latitude and longitude domains. 

Instead of running code in a Jupyter notebook, we’re going to write our code in a text editor called Sublime and run our code in the terminal.

1. Download sublime [here](https://www.sublimetext.com/3). Click to OSX downloader and follow the instructions. 
2. NumPy cheat sheet is [here](https://github.com/madesai22/ocean-ml/blob/master/cheat-sheets-resources/numpy-cheat-sheet.pdf)
3. NetCDF notebook from last week is [here](https://github.com/madesai22/ocean-ml/blob/master/NetCDF-tutorial_empty.ipynb)
	Quick NetCDF notes:
	* to import netCDF4 library: `from netCDF4 import Dataset`
	* to import netCDF file: `dataset = Dataset(r'/path/to/file')`
	* to access a data element: `lat = dataset['latitude']`

Note: BATS latitude range goes from 19.663 degrees North to 39.453 degrees North.
BATS longitude range goes from -59.648999999999994 degrees west (360 -59.648999999999994 degrees east) to 66.211 degrees west (360-66.211 degrees east)

Variables = vertical and horizontal velocities of specific lat/long
