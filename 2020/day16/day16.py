import re
with open("day16.txt") as f:
	lines = [line.rstrip() for line in f]
#print(lines)

# 20, 23
def part1(lines):
	minmax = []
	ticket_nums = []
	for ticket in lines[6:]:
		arr = re.findall(r'\d+', ticket)
		arr = list(map(int, arr))
		for i in arr:
			ticket_nums.append(i)
	print(ticket_nums)
	
	for s in lines[:3]:
		arr = re.findall(r'\d+', s)
		arr = list(map(int, arr))
		minmax.append((arr[0],arr[1]))
		minmax.append((arr[2],arr[3]))
	print(minmax)

	result = 0
	for num in ticket_nums:

		flag = False
		for idx, validation in enumerate(minmax):
			#print(num, i[0], i[1])
			if(num >= validation[0] and num <= validation[1]):

				flag = True
				break
		if(flag == False):
			result+= num
	print(result)

# part1(lines)
def check_validation(ticket_nums, minmax):
	result = 0
	valid_arr = []
	for nums_arr in ticket_nums:
		flags = []
		for num in nums_arr:
			flag = False
			for validation in minmax:
					
				if((num >= validation[0] and num <= validation[1]) or 
						(num >= validation[2] and num <= validation[3])):
					flag = True
					break
			if(flag==False):
				result+= num
				print(result)
			flags.append(flag)
		if(all(flags) == True):	
			valid_arr.append(nums_arr)
	return valid_arr

def part2(lines):
	minmax = []
	ticket_nums = []
	for ticket in lines[25:]:
		arr = re.findall(r'\d+', ticket)
		arr = list(map(int, arr))
		#print(arr)
		ticket_nums.append(arr)
	#print("TICKET_NUMS", ticket_nums)
	
	for s in lines[:20]:
		arr = re.findall(r'\d+', s)
		arr = list(map(int, arr))
		minmax.append((arr[0],arr[1], arr[2], arr[3]))
	#print("MINMAX", minmax)
	
	valid_arr = check_validation(ticket_nums, minmax)
	
	fields = {}
	len_validations = 20
	for i in range(len_validations):
		fields[i] = list(range(len_validations))
	print(fields)	
	for nums in valid_arr:

		flag = False
		for jdx, num in enumerate(nums):
			for idx, validation in enumerate(minmax):
				
				# print(num, idx, jdx)
				if((num >= validation[0] and num <= validation[1]) or 
					(num >= validation[2] and num <= validation[3])):
					continue
				elif(idx in fields[jdx]):
					fields[jdx].remove(idx)
	print("FIELDS", fields)

	match_dict = {}
	count = 0
	while(count < len_validations):
		for (key, field) in fields.items():
			if(len(field) == 1):
				match_dict[key] = field[0]
				count+=1
				to_remove = field[0]
				for (key2, value2) in fields.items():
					#print(count, to_remove, key2)
					if(to_remove in fields[key2]):
						fields[key2].remove(to_remove)
						#print(fields)
				#del fields[key]
				break

		print(match_dict)
		print(len(match_dict))
	return match_dict

match_dict = part2(lines)

def multiplyDepartureValues(match_dict):
	result = 1
	my_ticket = [97,101,149,103,137,61,59,223,263,179,131,113,241,127,53,109,89,173,107,211]
	for key, value in match_dict.items():
		if(value < 6):
			print(key, value)
			result*=my_ticket[key]
	print(result)

multiplyDepartureValues(match_dict)