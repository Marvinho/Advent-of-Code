import re

with open("test.txt") as f:
	##rules = f.read().rstrip()
	lines = [line.rstrip() for line in f]
	print(lines)

def handyHaversacks(lines):
	d = {}

	for line in lines:
		key_arr = line.split("bags contain")
		key = key_arr[0].strip()
		values = key_arr[1].split(",")
		values_arr = []
		color_d = {}
		for value in values:
			
			#print(value)
			words = value.strip().split(" ")
			if(words[0] != "no"):
				color_d[words[1]+" "+words[2]] = int(words[0])
		d[key] = color_d
	print(d)	
	s = set(["shiny gold"])
	l = -1
	while(len(s) > l):
		l = len(s)
		for key, value in d.items():
			#print( key, value)
			for i in s:
				if(i in value):
					s.add(key)
					break
			#print(s)
	print(s)
	print(len(s))

handyHaversacks(lines)