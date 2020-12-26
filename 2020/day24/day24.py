with open("day24.txt") as f:
	lines = [line.rstrip() for line in f]
# print(lines)

flipped_tiles = []
def part1(lines):
	for line in lines:
		count = 0
		mem = ""
		pos = [0, 0]#{"": 0, "y": 0}x
		for direction in line:
			# print("DIRECTION", direction)
			if(direction in "sn" and mem == ""):
				mem = direction
				# print("MEM:", mem)

			elif(direction in "ew" and mem == ""):
				if(direction == "e"):
					pos[0]+=2
					mem = ""
				if(direction == "w"):
					pos[0]-=2
					mem = ""


			elif(direction in "ew" and mem in "ns"):
				# print("MEM", mem)
				if(mem == "n" and direction == "e"):
					pos[0] += 1
					pos[1] += 1
				if(mem == "n" and direction == "w"):
					pos[0] -= 1
					pos[1] += 1
				if(mem == "s" and direction == "e"):
					pos[0] += 1
					pos[1] -= 1
				if(mem == "s" and direction == "w"):
					pos[0] -= 1
					pos[1] -= 1
				mem = ""
		if(pos in flipped_tiles):
			flipped_tiles.remove(pos)
		else:
			flipped_tiles.append(pos)
part1(lines)
print(flipped_tiles)
print(len(flipped_tiles))

def part2(lines):
	pass

