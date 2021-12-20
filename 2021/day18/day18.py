import math
with open("testday18-0.txt") as f: 
	numbers = []
	for line in f:
		line = line.strip()
		numbers.append(line)
print(numbers)
numbers_list = []
for number in numbers:
	new_numbers = []
	for x in number:
		if(x.isdigit()):
			new_numbers.append(int(x))
		else:
			new_numbers.append(x)
	numbers_list.append(new_numbers)
print(numbers_list)
def add(number1, number2):
	number1.append(",")
	number1.extend(number2)
	number1.append("]")
	number1.insert(0, "[")
	# number_list = list(number_str)
	print(number1)
	return number1


def reduce(number_list):
	while(True):
		changed = False
		stack = 0
		for i, number in enumerate(number_list):
			# print(stack, i , number)
			if(stack>4):
				if(isinstance(number, int) and isinstance(number_list[i+2], int)):
					stack = 0
					# print(i, number)
					number_list = explode(number_list, i, i+2)
					changed = True
					break
			if(number== "["):
				stack+= 1
			elif(number=="]"):
				stack-=1
		for i, number in enumerate(number_list):
			if(changed == True):
				break
			if(isinstance(number, int)):
				if(number>=10):
					number_list = split(number_list, i)
					changed = True
					break
		if(changed == False):
			break
	# print(number_list)
	return number_list

def explode(number_list , pos1, pos2):
	# print("EXPLODE")
	to_add1 = int(number_list[pos1])
	to_add2 = int(number_list[pos2])
	for i in range(pos1)[::-1]:
		if(isinstance(number_list[i], int)):
			number_list[i] = number_list[i]+ to_add1
			break
	for i in range(pos2+1, len(number_list)):
		if(isinstance(number_list[i], int)):
			number_list[i] = number_list[i]+ to_add2
			break
	number_list[pos1-1] = 0
	del number_list[pos1:pos2+2]
	# print(number_list)
	return number_list

def split(number_list, pos):
	# print("SPLIT")
	to_split = number_list[pos]
	left_ele = to_split//2
	right_ele = math.ceil(to_split/2)
	insert = []
	insert.append("[")
	insert.append(left_ele)
	insert.append(",")
	insert.append(right_ele)
	insert.append("]")
	number_list = number_list[:pos] + insert + number_list[pos+1:]
	# print(number_list)
	return number_list

def magnitude(number_list):
	while(True):
		changed = False
		for i, number in enumerate(number_list[:-2]):
			# print(number, number_list[i+2])
			if(isinstance(number, int) and isinstance(number_list[i+2], int)):
				# print("askfgsdahk")
				new_number = number*3 + number_list[i+2]*2
				number_list = number_list[:i-1]+[new_number]+number_list[i+4:]
				changed = True
				break
		# print(number_list)
		if(changed==False):
			break
	return number_list
def part2(numbers_list):
	asdf = numbers_list.copy()
	lst = []
	for i in asdf[0:10]:
		for j in asdf[0:10]:
			print(i)
			print()
			print(j)
			if(i==j):
				continue
			nlist = add(i, j)
			nlist = reduce(nlist)
			nlist = magnitude(nlist)
			lst.extend(nlist)
	print(lst)
if __name__ == '__main__':
	part2(numbers_list)

	# number_list = numbers_list[0]
	# for number in numbers_list[1:]:
	# 	number_list = add(number_list, number)
	# 	number_list = reduce(number_list)
	# 	print("NEXTTTTTTTTTTTTTTTTTTTTTTTTTT")
	# print(number_list)
	# magn = magnitude(number_list)
	# print(magn)