with open("day12.txt") as f:
	lines = [line.rstrip() for line in f]
print(lines)


def part1(lines):
	d = {0: "E", 1: "S", 2: "W", 3: "N"}
	direction = 0
	x = 0
	y = 0
	for line in lines:
		#print(line)
		if(line[0] == "N"):
			y+= int(line[1:])
		if(line[0] == "S"):
			y-= int(line[1:])
		if(line[0] == "E"):
			x+= int(line[1:])
		if(line[0] == "W"):
			x-= int(line[1:])
		if(line[0] == "R"):
			direction = int((direction + (1/90) * int(line[1:]))%4)
		if(line[0] == "L"):
			direction = int((direction - (1/90) * int(line[1:]))%4)
		if(line[0] == "F"):
			if(d[direction] == "N"):
				y+= int(line[1:])
			if(d[direction] == "S"):
				y-= int(line[1:])
			if(d[direction] == "E"):
				x+= int(line[1:])
			if(d[direction] == "W"):
				x-= int(line[1:])
		#print(direction, x, y)
	print(abs(x) + abs(y))

def part2(lines):
	waypoint = [10, 1]
	coord = [0, 0]
	for line in lines:
		if(line[0] == "N"):
			waypoint[1] += int(line[1:])
		if(line[0] == "S"):
			waypoint[1]-= int(line[1:])
		if(line[0] == "E"):
			waypoint[0]+= int(line[1:])
		if(line[0] == "W"):
			waypoint[0]-= int(line[1:])

		if(line == "R90" or line == "L270"):
			reminder = waypoint[0]
			waypoint[0] = waypoint[1]
			waypoint[1] = reminder * -1
		if(line == "R180" or line == "L180"):
			waypoint[0] = waypoint[0] *-1
			waypoint[1] = waypoint[1] * -1
			
		if(line == "R270" or line == "L90"):
			reminder = waypoint[0]
			waypoint[0] = waypoint[1] *-1
			waypoint[1] = reminder
		#print(waypoint)
		if(line[0] == "F"):
			coord[0] += int(line[1:])*waypoint[0]
			coord[1] += int(line[1:])*waypoint[1]
		print(waypoint, coord)
	print(abs(coord[0]) + abs(coord[1]))
part2(lines)