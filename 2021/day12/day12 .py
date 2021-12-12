with open("testday12-0.txt") as f:
	paths = {}
	caves = {}
	for c in f:
		c = c.strip().split("-")
		# print(c)
		caves[c[0]] = c[0].isUpper()
		paths[c[0]] = c[1]
		# paths.append(c.strip())
print(caves, paths)