with open("day23.txt") as f:
	lines = [line.rstrip() for line in f]
# print(lines)
cups = [int(i) for i in lines[0]]
print(cups)

def part1(cups):
	current_label = cups[0]
	pick_up = cups[1:4]
	cups_wout_pickups = [a for a in cups if a not in pick_up]
	
	dest_label = current_label-1
	while(dest_label in pick_up):
		dest_label = (dest_label - 1) % len(cups)

	cups = cups_wout_pickups[:cups_wout_pickups.index(dest_label)+1] + pick_up + cups_wout_pickups[cups_wout_pickups.index(dest_label)+1:]
	print("cups:",cups)
	print("pick up:",pick_up)
	print("destination:",dest_label)


	for i in range(99):
		current_label = cups[(cups.index(current_label) + 1) % len(cups)]
		current_pos = cups.index(current_label)
		# print("current label, pos:", current_label, current_pos)
		temp = cups + cups+cups[:3]
		# print("temp", temp)
		pick_up = temp[current_pos+1:current_pos+4]
		# print("pickup:", pick_up)
		cups_wout_pickups = [a for a in cups if a not in pick_up]
		# print("cups_wout:", cups_wout_pickups)
		dest_label = current_label
		while(dest_label in pick_up or dest_label == current_label):
			dest_label = (dest_label - 1) % len(cups)
			if(dest_label == 0):
				dest_label = len(cups)
		# print("dest_label:", dest_label)
		print("cups:", cups)
		cups = cups_wout_pickups[:cups_wout_pickups.index(dest_label)+1] + pick_up + cups_wout_pickups[cups_wout_pickups.index(dest_label)+1:]

		
		print("pick up:",pick_up)
		print("destination:",dest_label)
	print("final cups:", cups)
	return cups

def create_result_string(cups):
	print(cups, cups[cups.index(1)+1:], cups[:cups.index(1)])
	result = cups[cups.index(1)+1:] + cups[:cups.index(1)]
	return "".join(str(i) for i in result)
cups = part1(cups)
result = create_result_string(cups)
print(result)
