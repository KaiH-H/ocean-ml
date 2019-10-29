# Welcome back!

import numpy as np

# Print a while loop that prints 1-12
i = 1
while i < 13:
	print(i)
	i += 1

# Reviewing While loops:
# Write code to print multiples of 5 from 45 to 90

i = 45 
while i < 91:
	print(i)
	i += 5

# With your partner: discuss: What is a set? What is it good for?
# Write your response as a comment here:

# A set is an unordered group of things that cannot have duplicates

# Create a variable called "myset" and put whatever you want in it:

myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# Create a 2D numpy array of size 3x5 with numbers 1-15:

array = np.arange(1,16).reshape(3,5)
print(array)

# From your array, print the number 7:

print(array[1,1])

# Challenge: use while loop to print the following pattern:
# ****
# ***
# **
# *

star = ("*")
i = 0

while i < 4:
	print("*")
	star += "*"
	i += 1


