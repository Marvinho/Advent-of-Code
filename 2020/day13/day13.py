import numpy as np

with open("day13.txt") as f:
	lines = [line.rstrip() for line in f]
print(lines)

def part1(lines):
	depart_time = int(lines[0])
	bus_ids = lines[1].split(",")
	bus_arr = []
	for bus_id in bus_ids:
		try:
			bus_arr.append(int(bus_id))
		except:
			pass
	bus_arr = np.array(bus_arr)
	depart_arr = np.full(len(bus_arr), depart_time)
	print(depart_arr)
	print(bus_arr)
	wait_times = bus_arr - depart_arr % bus_arr
	shortest_wait = min(wait_times)
	itemindex = np.where(shortest_wait == wait_times)
	print(bus_arr[itemindex])
	result = bus_arr[itemindex] * shortest_wait
	print(result)
# part1(lines)

def part2(lines):
	# bus_ids = lines[1].split(",")
	# bus_arr = []
	# for i, bus_id in enumerate(bus_ids):
	# 	try:
	# 		bus_arr.append([i, int(bus_id)])
	# 	except:
	# 		pass
	# print(bus_arr)

	# for j in range(100000000000000, 200000000000000):
	# 	if(j % bus_arr[0][1] == 0):
	# 		arr = [(bus[1] - j % bus[1]) - bus[0] == 0 for bus in bus_arr[1:]]
	# 		if(all(arr) == True):
	# 			print(j)
	# 			break

part2(lines)
# print((13 - 3417 % 13) - 2 == 0)