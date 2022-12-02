with open("day01.txt") as f:
	depths = [line.rstrip() for line in f]

print(depths)
elfNr = 0
elfSum = {}
for i in depths:
	if(i == ''):
		elfNr+=1
	else:
		if(elfNr in elfSum):
			elfSum[elfNr]+= int(i)
		else:
			elfSum[elfNr] = int(i)
print(elfSum)

value = sorted(elfSum, key=elfSum.get, reverse=True)[:3]
result = 0
for i in value:
	result +=elfSum[i]
	print(elfSum[i])
print(result)