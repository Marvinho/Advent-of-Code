import numpy as np
with open("testday15.txt") as f:
	risk_levels = []
	for line in f:
		risk_levels.append([int(l) for l in line.strip()])
	# print(risk_levels)

risk_levels = np.array(risk_levels)
risk_levels = np.pad(risk_levels, pad_width=1, mode='constant', constant_values=-1)

print(risk_levels[0][2])
goal = risk_levels.shape
leny, lenx = risk_levels.shape[0], risk_levels.shape[1]
openlist = {(0, 0): (0, 20, 0)}
closedlist = {}

##########################################################
# Baue graph und finde besten path
# A*
##########################################################

def astar(risk_levels):
	
	while(len(openlist)>0):
		minimum = (0,0, 999999999)
		for key, value in openlist.items():
			if(value[2] < minimum[2]):
				minimum = value
				minimum_pos = key
		currentNode = openlist.pop(minimum_pos)
		closedlist[minimum_pos] = currentNode
		print(currentNode)
		if(minimum_pos == goal):
			print("path_found")
			return fhaslkfhdsklfdh
		
		expandNode(currentNode)

def expandNode(currentNode):
	successors = {}
	posy, posx = currentNode[0], currentNode[1]
	succ = [(0,1), (1,0), (0,-1), (-1,0)]
	for i in succ:
		to_add = (posy+i[0], posx+i[1], risk_levels[posy++i[0]][posx+i[1]])
		if(to_add[2]==-1):
			continue
		else:
			successors.append(to_add)
	for s in successors:
		if(s in closedlist):
			continue
		s[2] = currentNode[2] + s[2]
		childh = risk_levels[0]-s[0] + risk_levels[1]-s[1]
		childf = childh+childg
		if(s in openlist):
			if(s[2])
			continue
		s[2] = tent_g


	# successors = 