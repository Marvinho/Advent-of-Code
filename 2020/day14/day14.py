import re

with open("day14.txt") as f:
	lines = [line.rstrip() for line in f]
print(lines)

def part1(lines):
	mem = {}
	for line in lines:
		if(line[:4] == "mask"):
			mask_set = line[7:].replace("X","0")
			mask_clear = line[7:].replace("X","1")
			mask_set = int(mask_set, 2)
			mask_clear = int(mask_clear, 2)
			print(mask_set, mask_clear)
		if(line[:3] == "mem"):
			arr = list(map(int, re.findall('\d+', line)))
			num = (arr[1] | mask_set) & mask_clear
			mem[arr[0]] = num
	print(mem)
	print(sum(mem.values()))

part1(lines)