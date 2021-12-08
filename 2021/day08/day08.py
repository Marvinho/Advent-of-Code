with open("testday08.txt") as f:
	pattern_lst = []
	digit_output_lst = []
	for line in f:
		patterns, digit_output = line.strip().split("|")
		pattern_lst.append([pattern for pattern in patterns.split()])
		digit_output_lst.append(digit_output.strip().split())
		# print(digit_output_lst)
	# print(pattern_lst)

def easy_digits(pattern_lst, digit_output_lst):
	count = 0
	# for patterns in pattern_lst:
	# 	for pattern in patterns:
	# 		# print(pattern)
	# 		if(len(pattern)==2 or len(pattern)==3 or len(pattern) == 7):
	# 			count+=1
	for digits in digit_output_lst:
		for digit in digits:
			if(len(digit)==2 or len(digit)==3 or len(digit)==4 or len(digit) == 7):
				count+=1
	print(count)
	return count
# easy_digits(pattern_lst, digit_output_lst)
def calc_output_value(outputs, pattern_digit_map):
	output_str = ""
	for digit_str in outputs:
		# print(digit_str)
		for key, value in pattern_digit_map.items():
			if(set(digit_str) == value):
				output_str += str(key)
				break
	# print(output_str)
	return int(output_str)


def determine_digits(pattern_lst, digit_output_lst):
	whole_lst = [a + b for a, b in zip(pattern_lst, digit_output_lst)]
	print(whole_lst)
	pattern_digit_map = {-6:[], -5:[]}
	for digits in whole_lst:
		for digit in digits:
			match len(digit):
				case 2:
					pattern_digit_map[1]= set(digit)
				case 3:
					pattern_digit_map[7]= set(digit)
				case 4:
					pattern_digit_map[4]= set(digit)
				case 5:
					pattern_digit_map[-5].append(set(digit))
				case 6:
					pattern_digit_map[-6].append(set(digit))
				case 7:
					pattern_digit_map[8]= set(digit)
		for i in pattern_digit_map[-6]:
			if(i & pattern_digit_map[4] == i):
				pattern_digit_map[9] = i
			if(len(i & pattern_digit_map[1]) == 2):
				pattern_digit_map[0] = i
			if(len(i & pattern_digit_map[1]) == 1):
				pattern_digit_map[6] = i
		for i in pattern_digit_map[-5]:
			if(len(i & pattern_digit_map[6]) == 5):
				pattern_digit_map[5] = i
			if(len(i & pattern_digit_map[1]) == 2):
				pattern_digit_map[3] = i
			if(len(i & pattern_digit_map[4]) == 2):
				pattern_digit_map[2] = i
		del pattern_digit_map[-6]
		del pattern_digit_map[-5]
		print(pattern_digit_map)
		print(digits[-4:])
		output_lst = []
		output_lst.append(calc_output_value(digits[-4:], pattern_digit_map))
		print(sum(output_lst))

def calc_score():
	pass
determine_digits(pattern_lst, digit_output_lst)

	
