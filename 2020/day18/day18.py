import numpy as np
with open("test.txt") as f:
	lines = [line.rstrip().replace(" ", "") for line in f]
# print(lines)

# def part1(lines):
# 	for line in lines[:1]:
# 		openbr = 0
# 		rem = 0
# 		i = 0
# 		arr = []
# 		while(i < len(line)):
# 			if(openbr == 0 and line[i] == "("):
# 				arr.append(line[rem:i])
# 				openbr +=1
# 				rem = i
# 			elif(line[i] == "("):
# 				openbr += 1
# 			elif(line[i] == ")"):
# 				openbr -= 1
# 				if(openbr == 0):
# 					arr.append(line[rem:i+1])
# 					rem = i+1

# 			i+=1
# 			print(arr)

a = lines[0]
a = [i for i in a]
# def reduce(i, eq):
# 	arr = []
# 	while(i < len(eq)):
# 		if(eq[i] in "0123456789+*"):
# 			arr.append(eq[i])
# 			i+=1
# 		elif(c in "("):
# 			i, x = reduce(i+1, eq)
# 			arr.append(x)
# 		elif(c in ")"):

# 		i+=1
def solve(a):
	d = {0:[],1:[],2:[],3:[]}
	level = 0
	for i in a:
		if(i in "1234567890+*"):
			d[level].append(i)
		if(i in "("):
			level+= 1
		if(i in ")"):
			level-=1
	print(d)
solve(a)