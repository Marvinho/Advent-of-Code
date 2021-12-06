import numpy as np
with open("day06.txt") as f:
	for line in f:
		fishes = line.strip().split(",")
		fishes = [int(x) for x in fishes]

def lanternfish_grow(fishes, days):
	fish_count = [0]*9
	for fish in fishes:
		fish_count[fish] += 1
	print(fish_count)

	for i in range(0, days):
		temp = fish_count.pop(0)
		fish_count.append(temp)
		fish_count[6] += temp
		print("day ", i+1, fish_count)
	return fish_count
# asdf = [1,2,3,4]
# print(asdf-1)
score = sum(lanternfish_grow(fishes, 256))
print(score)
# lanternfish_grow(fishes)