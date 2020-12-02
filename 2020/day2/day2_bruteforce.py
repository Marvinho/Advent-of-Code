import re

with open("day2_input.txt") as f:
	lines = [line.rstrip() for line in f]
	#lines = list(map(int, lines))
	#print(lines)

def pwPhil(lines):
	result = 0
	for i in lines:
		lst = re.split("\W+", i)
		print(lst)
		lower = int(lst[0])
		upper =  int(lst[1])
		letter =  lst[2]
		pw =  lst[3]
		if(lower <= pw.count(letter) and upper >= pw.count(letter)):
			result +=1
	return result

#result = pwPhil(lines)
#print(result)

def pwPhil2(lines):
	result = 0
	for i in lines:
		lst = re.split("\W+", i)
		pos1 = int(lst[0])
		pos2 =  int(lst[1])
		letter =  lst[2]
		pw =  lst[3]
		if((pw[pos1-1] == letter) != (pw[pos2-1] == letter)):
			result+=1
	return result
result = pwPhil2(lines)
print(result)