with open("test2.txt") as f:
	##rules = f.read().rstrip()
	lines = sorted([int(line.rstrip()) for line in f])
print(lines)

def part1(lines):
	diffs = [0, 0, 1]
	reminder = 0


	for i in lines:
		if(i - reminder == 1):
			diffs[0] += 1
		elif(i- reminder == 2):
			diffs[1] += 1
		elif(i-reminder == 3):
			diffs[2] += 1
		reminder = i
	print(diffs)
	print(diffs[0]*diffs[2])

part1(lines)