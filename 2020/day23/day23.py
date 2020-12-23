import time

with open("day23.txt") as f:
	lines = [line.rstrip() for line in f]
# print(lines)
cups = [int(i) for i in lines[0]]
# print(cups)

part_no = 2
def create_cup_dict(cups):
	cups_dict = {}
	for i in range(len(cups)):
		cups_dict[cups[i]] = cups[(i+1)%len(cups)]
	
	if(part_no == 2):
		cups += [i for i in range(len(cups)+1, 1000001)]
		for i in range(len(cups)):
			cups_dict[cups[i]] = cups[(i+1)%len(cups)]
		print(cups_dict[1000000])	
	
	return cups_dict

def part2(cups_dict, current_label):
	if(part_no == 2):
		iterations = 10000000
	else:
		iterations = 100
	start = time.time()
	for i in range(iterations):
		# print("cups: ", cups_dict)
		pickups = []
		pickups.append(cups_dict[current_label])
		pickups.append(cups_dict[cups_dict[current_label]])
		pickups.append(cups_dict[cups_dict[cups_dict[current_label]]])
		next_current = cups_dict[cups_dict[cups_dict[cups_dict[current_label]]]]
		dest_label = current_label
		while(dest_label in pickups or dest_label == current_label):
			dest_label = (dest_label-1) % len(cups)
			if(dest_label == 0):
				dest_label = len(cups)


		temp = cups_dict[dest_label]			
		cups_dict[dest_label] = pickups[0]
		cups_dict[pickups[0]] = pickups[1]
		cups_dict[pickups[1]] = pickups[2]
		cups_dict[pickups[2]] = temp
		# print(next_current)
		cups_dict[current_label] = next_current
		
		# print("cups: ", cups_dict)
		# print("current: ", current_label)
		# print("pick up: ", pickups)
		# print("destination: ", dest_label)
		
		current_label = cups_dict[current_label]

		# if(i == 1000000):
		# 	print(time.time() - start)
		# 	break
	# print(cups_dict)
	return cups_dict

def create_result_string(cups_dict):
	i = cups_dict[1]
	result_str = ""
	while(i != 1):
		result_str += str(i)
		i = cups_dict[i]
	print(result_str)
	return result_str

def create_result_multiplying(cups_dict):
	result = cups_dict[1] * cups_dict[cups_dict[1]]
	print(result
		)
cups_dict = create_cup_dict(cups)
current_label = cups[0]
cups_dict = part2(cups_dict, current_label)
create_result_multiplying(cups_dict)
# create_result_string(cups_dict)

# def part1(cups):
# 	current_label = cups[0]
# 	pickups_up = cups[1:4]
# 	cups_wout_pickups = [a for a in cups if a not in pickups_up]
	
# 	dest_label = current_label-1
# 	while(dest_label in pickups_up):
# 		dest_label = (dest_label - 1) % len(cups)

# 	cups = cups_wout_pickups[:cups_wout_pickups.index(dest_label)+1] + pickups_up + cups_wout_pickups[cups_wout_pickups.index(dest_label)+1:]
# 	# print("cups:",cups)
# 	# print("pickups up:",pickups_up)
# 	# print("destination:",dest_label)


# 	for i in range(10):
# 		current_label = cups[(cups.index(current_label) + 1) % len(cups)]
# 		current_pos = cups.index(current_label)
# 		# print("current label, pos:", current_label, current_pos)
# 		temp = cups + cups+cups[:3]
# 		# print("temp", temp)
# 		pickups_up = temp[current_pos+1:current_pos+4]
# 		# print("pickupsup:", pickups_up)
# 		cups_wout_pickups = [a for a in cups if a not in pickups_up]
# 		# print("cups_wout:", cups_wout_pickups)
# 		dest_label = current_label
# 		while(dest_label in pickups_up or dest_label == current_label):
# 			dest_label = (dest_label - 1) % len(cups)
# 			if(dest_label == 0):
# 				dest_label = len(cups)
# 		# print("dest_label:", dest_label)
# 		# print("cups:", cups)
# 		cups = cups_wout_pickups[:cups_wout_pickups.index(dest_label)+1] + pickups_up + cups_wout_pickups[cups_wout_pickups.index(dest_label)+1:]

		
# 	# 	print("pickups up:",pickups_up)
# 	# 	print("destination:",dest_label)
# 	# print("final cups:", cups)
# 	return cups


