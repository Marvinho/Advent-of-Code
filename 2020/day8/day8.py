import copy

with open("day8.txt") as f:
	##rules = f.read().rstrip()
	lines = [line.rstrip() for line in f]
	#print(lines)
print(lines)
d = {}
accumulator = 0
# arr = []
# for i in lines:
# 	arr.append([i.split()[0], int(i.split()[1]), 0])
# print(arr)

def part1(arr, accumulator):
	j = 0
	while(j < len(arr)):
		print(arr[j])

		if(arr[j][2] == 1):
			break
		arr[j][2] = 1
		if(arr[j][0] == "nop"):
			j+=1
		elif(arr[j][0] == "jmp"):
			j+= arr[j][1]
		elif(arr[j][0] == "acc"):
			accumulator+= arr[j][1]
			j+=1
		
	return accumulator

#accumulator = part1(arr, accumulator)
#print(accumulator)
accumulator = 0
arr = []
for i in lines:
	arr.append([i.split()[0], int(i.split()[1])])
print(arr)

def part2(arr, accumulator):
	arr1 = copy.deepcopy(arr)
	for idx, i in enumerate(arr1):
		arr = copy.deepcopy(arr1)
		if(arr[idx][0] == "nop"):
			# print("asdf")
			arr[idx][0] = "jmp"
		elif(arr[idx][0] == "jmp"):
			arr[idx][0] = "nop"
		else:
			continue
		j = 0
		counter = 0
		accumulator = 0
		while(j < len(arr)):

			#print(arr[j])
			if(arr[j][0] == "nop"):
				j+=1
			elif(arr[j][0] == "jmp"):
				j+= arr[j][1]
			elif(arr[j][0] == "acc"):
				accumulator+= arr[j][1]
				j+=1
			# if(counter < 10):
			# 	print(accumulator)
			counter+=1
			if(counter > 99999):
				accumulator = None
				break
		if(accumulator != None):
			print(accumulator)
	return accumulator	
accumulator = part2(arr, accumulator)
print(accumulator)