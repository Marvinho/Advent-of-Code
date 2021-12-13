import numpy as np
with open("day13.txt") as f:
	dots = []
	fold_instructions = []
	for line in f:
		line = line.strip()
		if("fold" in line):
			direction, pos = line.split("=")
			fold_instructions.append((direction[-1],int(pos)))
		elif(len(line) < 1):
			continue
		else:
			line = [int(x) for x in line.split(",")]
			dots.append(line)
	print(dots, fold_instructions)
max_size = np.amax(dots)
dot_arr = np.zeros((max_size+1,max_size+1), dtype=int)
for y, x in dots:
	dot_arr[x][y] = 1
print(dot_arr)
def fold(dot_arr, fold_instructions, n=1):
	for i in range(n):
		# print(dot_arr.shape)
		# print(fold_instructions[i])
		if("y" in fold_instructions[i][0]):
			fold_line = fold_instructions[i][1]+1
			half = dot_arr[fold_line:fold_line*2-1][:]
			half = half[::-1]
			print(dot_arr.shape)
			dot_arr = dot_arr[:fold_line-1]
			print(half.shape, dot_arr.shape)
			dot_arr = np.add(dot_arr, half)
			print(dot_arr)
		elif("x" in fold_instructions[i][0]):
			# print(fold_instructions[i])
			# print(dot_arr)
			fold_line = fold_instructions[i][1]+1
			# print(fold_line, dot_arr.shape)
			half = dot_arr[:, fold_line:fold_line*2-1]
			# print("half",half)
			half = np.flip(half, 1)
			# print("halfrev", half)
			dot_arr = dot_arr[:, :fold_line-1]
			# print(dot_arr)
			dot_arr = np.add(dot_arr, half)
			print(dot_arr)
	dot_arr[dot_arr >= 1]="1"				
	print(dot_arr)
	return dot_arr
		# print(np.sum(dot_arr))


dot_arr = fold(dot_arr, fold_instructions, len(fold_instructions))
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

ax = sns.heatmap(dot_arr, annot=True, fmt="d")

plt.title("How to visualize (plot) \n a numpy array in python using seaborn ?",fontsize=12)

plt.savefig("visualize_numpy_array_01.png", bbox_inches='tight', dpi=100)

plt.show()