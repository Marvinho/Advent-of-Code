import numpy as np
with open("day06.txt") as f:
	for line in f:
		fishes = line.strip().split(",")
		fishes = [int(x) for x in fishes]

def lanternfish_grow(fishes, days):
	print(fishes)
	for i in range(0, days):
		count = 0
		for j, fish in enumerate(fishes):
			fishes[j] -= 1
			if(fishes[j] == -1):
				fishes[j] = 6
				count+=1
		for j in range(count):
			fishes.append(8)
		# print("Day {}: {}".format(i+1, fishes))
	return fishes

asdf = [1,2,3,4]
print(asdf-1)
# score = len(lanternfish_grow(fishes, 256))
print(score)
# lanternfish_grow(fishes)