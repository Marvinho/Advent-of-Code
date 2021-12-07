import math
with open("testday07.txt") as f:
	for line in f:
		h_positions = line.strip().split(",")
		h_positions = [int(x) for x in h_positions]
print(h_positions)

def align_horizontally(h_positions):
	h_pos_dict = {key: 0 for key in h_positions}
	for pos in h_positions:
		h_pos_dict[pos] += 1
	print(h_pos_dict)
	min_fuel_used = sum(h_positions)+1
	print(min_fuel_used)
	for i in range(0, max(h_positions)):
		fuel_used = 0
		for key, value in h_pos_dict.items():
			fuel_used += abs(i*value - key*value)
		if(fuel_used < min_fuel_used):
			min_fuel_used = fuel_used
			print(fuel_used)
		else:
			print("min",min_fuel_used)
			return min_fuel_used

min_fuel_used = align_horizontally(h_positions)