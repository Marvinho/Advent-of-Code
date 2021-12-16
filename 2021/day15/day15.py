import numpy as np
with open("day15.txt") as f:
	risk_levels = []
	for line in f:
		risk_levels.append([int(l) for l in line.strip()])
	# print(risk_levels)

risk_levels = np.array(risk_levels)
# risk_levels = np.pad(risk_levels, pad_width=1, mode='constant', constant_values=-1)

# print(risk_levels[0][2])
goal = risk_levels.shape
leny, lenx = risk_levels.shape[0], risk_levels.shape[1]
openlist = {(0, 0): (0, 20, 0)}
closedlist = {}

def part2(risk_levels):
	new_risk_levels = np.copy(risk_levels)
	# print(new_risk_levels, risk_levels)
	for j in range(1,5):
		new_risk_levels = np.concatenate((new_risk_levels, risk_levels+j), axis=0)
		# new_risk_levels[new_risk_levels  10] = 1
	new_risk_levels1 = np.copy(new_risk_levels)
	for i in range(1,5):
		new_risk_levels1 = np.concatenate((new_risk_levels1, new_risk_levels+i), axis=1)
	new_risk_levels1[new_risk_levels1 >= 10] = -9 + new_risk_levels1[new_risk_levels1 >= 10]
	# print(new_risk_levels1)
	return new_risk_levels1


def astar(risk_levels):
	# print(risk_levels, openlist)
	while(len(openlist)>0):
		minimum = (0,0,999999999)
		for key, value in openlist.items():
			# print(value)
			if(value[2] < minimum[2]):
				minimum = value
				currentNode = key
		closedlist[currentNode] = openlist[currentNode]
		del openlist[currentNode]
		
		# print(currentNode, (risk_levels.shape[0], risk_levels.shape[1]))
		if(currentNode == (risk_levels.shape[0]-1, risk_levels.shape[1]-1)):
			print("path_found")
			print(currentNode, closedlist[currentNode])
		
		expandNode(currentNode)

def expandNode(currentNode):
	successors = {}
	posy, posx = currentNode[0], currentNode[1]
	succ = [(0,1), (1,0), (0,-1), (-1,0)]
	for i in succ:
		to_add = (currentNode[0]+i[0], currentNode[1]+i[1])
		if(to_add[0]==-1 or 
			to_add[1]==-1 or 
			to_add[0]>=risk_levels.shape[0] or 
			to_add[1]>=risk_levels.shape[1]):
			continue
		else:
			successors[to_add] = (0, 0, 0)
	for s in successors:
		if(s in closedlist):
			continue
		childg = closedlist[currentNode][0] + risk_levels[s[0]][s[1]]
		# print(s)
		childh = -2+risk_levels.shape[0] +risk_levels.shape[1] - s[0]-s[1]
		childf = childh+childg
		# print(childg, childh, childf)
		if(s in openlist):
			if(childf > openlist[s][2]):
				continue
		if(s in closedlist):
			if(childf > closedlist[s][2]):
				continue

		# print(openlist)
		# print(risk_levels[s[0]][s[1]])
		openlist[s] = (childg, childh, childf)

	# successors = 
if __name__=="__main__":
	risk_levels = part2(risk_levels)
	print(risk_levels.shape)
	astar(risk_levels)
	# print(a, b)