import numpy as np
import math

with open("day3_input.txt") as f:
	lines = [line.rstrip() for line in f]

slopes =[(1,1), (3,1), (5,1), (7,1), (1,2)]

def trajectory(lines, slopes):
	results = []
	for slope in slopes:
		pos=0
		trees = 0
		#print(slope)
		for row in lines[::slope[1]]:
			#print(row, row[pos%len(row)])
			#print(row[pos%len(row)])
			if(row[pos%len(row)] == "#"):
				trees+=1
			pos+=slope[0]
		results.append(trees)
	return results

results = trajectory(lines, slopes)
start = results[0]
for i in results[1:]:
	start*=i
print(start)

