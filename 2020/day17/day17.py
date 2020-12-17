import numpy as np
with open("day17.txt") as f:
	lines = [line.rstrip() for line in f]
print(lines)
arr = []
for idx, line in enumerate(lines):
	line = line.replace(".","0")
	line = line.replace("#","1")
	arr.append([int(i) for i in line])



def checkNeighbours(b, i, j, k):
	active_count = 0
	for l in range(i-1, i+2):
		for m in range(j-1, j+2):
			for n in range(k-1, k+2):
				if(b[l][m][n] == 1):
					# print(l, m, n, b[l][m][n])
					active_count+=1
	return active_count

def cycleProcess1(a):
	for cycle in range(6):
		a = np.pad(a, (1,1))
		c = np.zeros(a.shape, dtype=int)
		#print(len(a), len(a[0]))
		for i in range(1, len(a)+1):
			for j in range(1, len(a[0])+1):
				for k in range(1, len(a[0][0])+1):
					b = np.pad(a, (1,1))
					active_count = checkNeighbours(b, i, j, k)
					#print(active_count)
					if(a[i-1][j-1][k-1] == 0):
						if(active_count == 3):
							c[i-1][j-1][k-1] = 1
					elif(a[i-1][j-1][k-1] == 1):
						if(active_count-1 == 2 or active_count-1 == 3):
							c[i-1][j-1][k-1] = 1
		#print(c)
		a = np.copy(c)
		print(np.sum(a))

def checkNeighbours2(b, i, j, k, h):
	active_count = 0
	for l in range(i-1, i+2):
		for m in range(j-1, j+2):
			for n in range(k-1, k+2):
				for o in range(h-1, h+2):
					if(b[l][m][n][o] == 1):
						# print(l, m, n, b[l][m][n])
						active_count+=1
	return active_count	
def cycleProcess2(a):
	for cycle in range(6):
		a = np.pad(a, (1,1))
		c = np.zeros(a.shape, dtype=int)
		for i in range(1, len(a)+1):
			for j in range(1, len(a[0])+1):
				for k in range(1, len(a[0][0])+1):
					for h in range(1, len(a[0][0][0])+1):
						b = np.pad(a, (1,1))
						active_count = checkNeighbours2(b, i, j, k, h)
						#print(active_count)
						if(a[i-1][j-1][k-1][h-1] == 0):
							if(active_count == 3):
								c[i-1][j-1][k-1][h-1] = 1
						elif(a[i-1][j-1][k-1][h-1] == 1):
							if(active_count-1 == 2 or active_count-1 == 3):
								c[i-1][j-1][k-1][h-1] = 1
		#print(c)
		a = np.copy(c)
		print(np.sum(a))

a = np.array(arr)
a = np.expand_dims(a, axis=0)
a2 = np.expand_dims(a, axis=0)
print(a.shape)
print(a)

# cycleProcess(a)
cycleProcess2(a2)