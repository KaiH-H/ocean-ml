
# 1. Use a while loop to print numbers 1-10:
num = 0
while num < 10:
	num += 1
	print(num)

# 2. Use a while loop to print the first 10 multiples of 24:
mult = 0
while mult < 240:
 	mult += 24
 	print(mult)

# 3. Use a while loop to find the average of these numbers:
numbers = [10,42,-2, 900,5,8,39]

index = 0
sum_numbers = 0

# for i in numbers:    --> For loop to get the basis for the while loop
# 	sum_numbers += i
# 	index += 1

length = len(numbers)

while index < length:
	sum_numbers += numbers[index]
	index += 1

avg = sum_numbers/index

print(avg)
