with open("day01.txt") as f:
	depths = [int(line.rstrip()) for line in f]
# print(depths)

def number_of_larger_measurements(depths):
	result = 0
	for i in range(len(depths)-1):
		if(depths[i] < depths[i+1]):
			result+=1
	return result
print(number_of_larger_measurements(depths))

def three_measurement_windows(depths):
	print(depths)
	result = 0
	for i, depth in enumerate(depths[:-3]):
		prev = depths[i]+ depths[i+1]+depths[i+2]
		now = depths[i+1]+ depths[i+2]+depths[i+3]
		print(prev, now)
		if(prev < now):
			result+=1
	return result

# print(three_measurement_windows(depths))