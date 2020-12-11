with open("day1_input.txt") as f:
	lines = [line.rstrip() for line in f]
	lines = list(map(int, lines))
	print(lines)
i = 1
result= 0
for number in lines:
	#print(number)
	for j in lines[i:]:
		#print(lines[i:])
		for k in lines[i+1:]:
			if(number+j+k == 2020):
				result = number*j*k
				break;
	i+=1
print(result)