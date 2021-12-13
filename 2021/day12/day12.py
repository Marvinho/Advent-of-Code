import networkx as nx
from collections import Counter
G = nx.Graph()
with open("day12.txt") as f:
	
	caves = {}
	small_caves = {}
	for c in f:
		c = c.strip().split("-")
		# print(c)
		G.add_edge(*c)

# print(G.nodes)
# print(G.edges)
stack = [["start"]]
def find_paths(last_node):
	score = 0
	while(stack):
		# print(stack)
		path = stack.pop(0)
		# print(path)
		# print("neighbors", list(G.neighbors(path[-1])))
		for node in G.neighbors(path[-1]):
			if(node == "end"):
				score+=1
			elif(node =="start"):
				continue
			elif(node.isupper()):
				stack.append(path+[node])
			elif(node not in path):
				stack.append(path+[node])
			elif(node.islower() and node in path):
				asdf = Counter(path)
				rep_list = []
				for k in asdf:
					if(k.islower()):
						rep_list.append(asdf[k])
				if(all(i < 2 for i in rep_list)):
					stack.append(path+[node])
	print(score)
find_paths(stack)