with open("testinput.txt") as f: 
	scanners = []
	for line in f:
		a = [l for l in line.strip().split("\n\n")]
		i = 0
		if(a[0]):
			if("scanner" in a[0]):
				i+=1
			else:
				scanners[0].append([int(x) for x in a[0].split(",")])
	print(scanners)