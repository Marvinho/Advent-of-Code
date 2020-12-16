import re
with open("day16.txt") as f:
	lines = [line.rstrip() for line in f]
#print(lines)


def part1(lines):
	minmax = []
	ticket_nums = []
	for ticket in lines[23:]:
		arr = re.findall(r'\d+', ticket)
		arr = list(map(int, arr))
		for i in arr:
			ticket_nums.append(int(i))
	print(ticket_nums)
	
	for s in lines[:20]:
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


part1(lines)