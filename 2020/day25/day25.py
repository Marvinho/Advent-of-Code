with open("day25.txt") as f:
	lines = [int(line.rstrip()) for line in f]
print(lines)

card_pub_key = lines[0]
door_pub_key = lines[1]

def determine_loopsize(key):
	subject_number = 7
	value = 1
	i = 1
	while(True):
		value *= subject_number
		value = value % 20201227
		if(value == key):
			print(i, value)
			loopsize = i
			break
		i+=1
	return loopsize

def calc_enc_key(subject_number, loopsize):
	value = 1
	for i in range(1, loopsize+1):
		value *= subject_number
		value = value % 20201227
	print(value)	
	return value
card_loop_size = determine_loopsize(card_pub_key)
door_loop_size = determine_loopsize(door_pub_key)

enc_key = calc_enc_key(door_pub_key, card_loop_size)
enc_key = calc_enc_key(card_pub_key, door_loop_size)
