with open("testday12-0.txt") as f:
	paths = {}
	caves = {}
	for c in f:
		c = c.strip().split("-")
		# print(c)
		caves[c[0]] = c[0].isupper()
		caves[c[1]] = c[1].isupper()
		if(c[0] not in paths):
			paths[c[0]] = {c[1]}
		else:
			paths[c[0]].add(c[1])
		if(c[1] not in paths):
			paths[c[1]] = {c[0]}
		else:
			paths[c[1]].add(c[0])
print(caves, paths)

def find_paths(paths, caves):
	paths_list = []
	for value in paths["start"]:
		paths_list.append(["start", value])
	print(paths_list)
	new_paths_list = paths_list[:]
	flag=True
	while(flag):
		flag=False
		paths_list = new_paths_list[:]
		new_paths_list = []
		for path in paths_list:
			for value in paths[path[-1]]:
				if((value not in path[:-1] or caves[value]==True) and path[-1]!="end"):
					new_paths_list.append(path+[value])
					flag=True
				elif(path[-1]=="end" and path not in new_paths_list):
					new_paths_list.append(path)
					# print(value, path)
					# new_paths_list.append(path)
		print(new_paths_list)
		# print(flag)
		print(len(new_paths_list))


find_paths(paths, caves)