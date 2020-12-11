import copy
import numpy as np
with open("day11.txt") as f:
	##rules = f.read().rstrip()
	lines = [line.rstrip() for line in f]
	lines = [list(line) for line in lines]
#print(lines)
def part1(lines):
	seats = np.array(lines)
	print(seats.shape)
	seats = np.pad(seats, pad_width = 1, mode = "constant", constant_values="-")
	print(seats)
	prev = []
	while(np.array_equal(prev, seats) == False):
		prev = np.copy(seats)
		for i in range(seats.shape[0]):
			for j in range(seats[i].shape[0]):
				#print(i, j)
				if(prev[i][j] == "." or prev[i][j] == "-"):
					continue
				elif(prev[i][j] == "L"):
						if(prev[i-1][j-1] != "#" and prev[i-1][j] != "#" and prev[i-1][j+1] != "#" and 
								prev[i][j-1] != "#" and prev[i][j] != "#" and prev[i][j+1] != "#" and 
								prev[i+1][j-1] != "#" and prev[i+1][j] != "#" and prev[i+1][j+1] != "#"):
								seats[i][j] = "#"
				elif(prev[i][j] == "#"):
					occupied = 0
					if(prev[i-1][j-1] == "#"):
						occupied+=1
					if(prev[i-1][j] == "#"):
						occupied+=1
					if(prev[i-1][j+1] == "#"):
						occupied+=1
					if(prev[i][j-1] == "#"):
						occupied+=1
					if(prev[i][j+1] == "#"):
						occupied+=1
					if(prev[i+1][j-1] == "#"):
						occupied+=1
					if(prev[i+1][j] == "#"):
						occupied+=1
					if(prev[i+1][j+1] == "#"):
						occupied+=1
					if(occupied >= 4):
						seats[i][j] = "L"
		print(seats)
		unique, counts = np.unique(seats, return_counts=True)
		print(dict(zip(unique, counts)))

# def part1(lines):
# 	lines2 = []
# 	while(lines != lines2):
# 		lines2 = copy.deepcopy(lines)
# 		for i in range(len(lines)):
# 			row = len(lines[i])
# 			for j in range(row):
# 				#print(lines2)
# 				if(lines2[i][j] == "."):
# 					continue
# 				elif(lines2[i][j] == "L"):
# 					if(i == 0):
# 						if(j == 0):
# 							if(lines2[i][j+1] != "#" and lines2[i+1][j] != "#" and lines2[i+1][j+1] != "#"):
# 								lines[i][j] = "#"
# 						elif(j == row-1):
# 							if(lines2[i][j-1] != "#" and lines2[i+1][j] != "#" and lines2[i+1][j-1] != "#"):
# 								lines[i][j] = "#"
# 						else:
# 							if(lines2[i][j+1] != "#" and lines2[i+1][j] != "#" and lines2[i+1][j+1] != "#" and 
# 								lines2[i][j-1] != "#" and lines2[i+1][j-1] != "#"):
# 								lines[i][j] = "#"

# 					if(i == len(lines)-1):
# 						if(j==0):
# 							if(lines2[i][j+1] != "#" and lines2[i-1][j] != "#" and lines2[i-1][j+1] != "#"):
# 								lines[i][j] = "#"
# 						elif(j==row-1):
# 							if(lines2[i][j-1] != "#" and lines2[i-1][j] != "#" and lines2[i-1][j-1] != "#"):
# 								lines[i][j] = "#"
# 						else:
# 							if(lines2[i][j+1] != "#" and lines2[i-1][j] != "#" and lines2[i-1][j+1] != "#" and 
# 								lines2[i][j-1] != "#" and lines2[i-1][j-1] != "#"):
# 								lines[i][j] = "#"
# 					else:
# 						if(j==0):
# 							if(lines2[i-1][j] != "#" and lines2[i-1][j+1] != "#" and lines2[i][j+1] != "#" and 
# 								lines2[i+1][j] != "#" and lines2[i+1][j+1] != "#"):
# 								lines[i][j] = "#"
# 						elif(j == row-1):
# 							if(lines2[i-1][j] != "#" and lines2[i-1][j-1] != "#" and lines2[i][j-1] != "#" and 
# 								lines2[i+1][j] != "#" and lines2[i+1][j-1] != "#"):
# 								lines[i][j] = "#"
# 						else:
# 							if(lines2[i-1][j-1] != "#" and lines2[i-1][j] != "#" and lines2[i][j+1] != "#" and 
# 								lines2[i][j-1] != "#" and lines2[i][j] != "#" and lines2[i][j+1] != "#" and 
# 								lines2[i+1][j-1] != "#" and lines2[i+1][j] != "#" and lines2[i+1][j+1] != "#"):
# 								lines[i][j] = "#"
# 				elif(lines2[i][j] == "#"):
# 					occupied = 0
# 						if(i == 0):
# 							if(j == 0):
# 								if(lines2[i][j+1] != "#" and lines2[i+1][j] != "#" and lines2[i+1][j+1] != "#"):
# 									lines[i][j] = "#"
# 							elif(j == row-1):
# 								if(lines2[i][j-1] != "#" and lines2[i+1][j] != "#" and lines2[i+1][j-1] != "#"):
# 									lines[i][j] = "#"
# 							else:
# 								if(lines2[i][j+1] != "#" and lines2[i+1][j] != "#" and lines2[i+1][j+1] != "#" and 
# 									lines2[i][j-1] != "#" and lines2[i+1][j-1] != "#"):
# 									lines[i][j] = "#"

# 						if(i == len(lines)-1):
# 							if(j==0):
# 								if(lines2[i][j+1] != "#" and lines2[i-1][j] != "#" and lines2[i-1][j+1] != "#"):
# 									lines[i][j] = "#"
# 							elif(j==row-1):
# 								if(lines2[i][j-1] != "#" and lines2[i-1][j] != "#" and lines2[i-1][j-1] != "#"):
# 									lines[i][j] = "#"
# 							else:
# 								if(lines2[i][j+1] != "#" and lines2[i-1][j] != "#" and lines2[i-1][j+1] != "#" and 
# 									lines2[i][j-1] != "#" and lines2[i-1][j-1] != "#"):
# 									lines[i][j] = "#"
# 						else:
# 							if(j==0):
# 								if(lines2[i-1][j] != "#" and lines2[i-1][j+1] != "#" and lines2[i][j+1] != "#" and 
# 									lines2[i+1][j] != "#" and lines2[i+1][j+1] != "#"):
# 									lines[i][j] = "#"
# 							elif(j == row-1):
# 								if(lines2[i-1][j] != "#" and lines2[i-1][j-1] != "#" and lines2[i][j-1] != "#" and 
# 									lines2[i+1][j] != "#" and lines2[i+1][j-1] != "#"):
# 									lines[i][j] = "#"
# 							else:
# 								if(lines2[i-1][j-1] != "#" and lines2[i-1][j] != "#" and lines2[i][j+1] != "#" and 
# 									lines2[i][j-1] != "#" and lines2[i][j] != "#" and lines2[i][j+1] != "#" and 
# 									lines2[i+1][j-1] != "#" and lines2[i+1][j] != "#" and lines2[i+1][j+1] != "#"):
# 									lines[i][j] = "#"

# 		print(lines)

part1(lines)