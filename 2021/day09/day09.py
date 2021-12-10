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
	pos_low_points = []
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
					# print(i, j)
					# print(column)
					low_points.append(column)
					pos_low_points.append((i, j))
	return low_points, pos_low_points



def locate_basins(i, j):
	print(i, j )
	
	score = 0
	if(heightmap[i][j] == 9 or (i==0 or i==heightmap.shape[0]-1 or 
								j==0 or j==heightmap.shape[1]-1)):
		return 0
	else:
		heightmap[i][j] = 9
		score+= 1
		# locate_basins()
		print(score)
		return (score + locate_basins(i, j-1) 
				+ locate_basins(i-1, j)
				+ locate_basins(i+1, j)
				+ locate_basins(i, j+1))

def calc_score (low_points):
	score = sum(low_points)+len(low_points)
	print(score)
	return score


# print(low_points)
# calc_score(low_points)

if __name__=="__main__":
	basins = []
	low_points, pos_low_points = part1(heightmap)
	for i, j in pos_low_points:
		basins.append(locate_basins(i, j))
	basins = sorted(basins)
	result = basins[-1]*basins[-2]*basins[-3]
	print(result)

