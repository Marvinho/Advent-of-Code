
tile_d = {}
match_d = {}
with open("day20.txt") as f:
	tiles = [line.rstrip() for line in f]
tiles.append("")
print(tiles)

for tile in tiles:
	if("Tile" in tile):
		tile_id = int(tile[5:-1])
		i = 0
		left = ""
		right = ""
		top = ""
		bottom = ""
	elif(len(tile)> 1):
		left+=tile[0]
		right+=tile[-1]
		if(i==0):
			top=tile
		if(i==9):
			bottom = tile
		i+=1

	else:
		tile_d[tile_id] = (top, bottom, left, right, 
						top[::-1], bottom[::-1], left[::-1], right[::-1])
print(tile_d)

for key, value in tile_d.items():
	for key2, value2 in tile_d.items():
		for v in value:
			for v2 in value2:
				if(v == v2):
					if(key in match_d):
						match_d[key] +=1
					else:
						match_d[key] = 1
print(match_d)

result = 1
for key, value in match_d.items():
	if(value == 12):
		print(key, value)
		result*=key
print(result)