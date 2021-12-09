import numpy as np
with open("day09.txt") as f:
	heightmap = []
	for line in f:
		heightmap.append([int(x) for x in line.strip()])

heightmap = np.asarray(heightmap)
heightmap = np.pad(heightmap, pad_width=1, mode='constant', constant_values=9)
print(heightmap.shape)
def part1(heightmap):
	print(heightmap)
	low_points = []
	row_len = heightmap.shape[1]-1
	column_len = heightmap.shape[0]-1
	for i, row in enumerate(heightmap):
		for j, column in enumerate(row):
			if(i==0 and i==row_len and j==0 and j==column_len):
				break
			else:
				if(column<heightmap[i][j-1] and 
					column<heightmap[i-1][j] and
					column<heightmap[i+1][j] and
					column<heightmap[i][j+1]):
					print(i, j)
					print(column)
					low_points.append(column)
	return low_points

def calc_score (low_points):
	score = sum(low_points)+len(low_points)
	print(score)
	return score
low_points = part1(heightmap)
print(low_points)
calc_score(low_points)