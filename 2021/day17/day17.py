with open("day17.txt") as f: 
	for line in f:
		targets = line.strip()[15:].split(", y=")
		print(targets)
		ts = []
		for target in targets:
			target = [int(x) for x in target.split("..")]
			ts.append(target)

print(ts)

def get_xtry(ts):
	xpos, ypos = 0, 0
	xtry = []
	for i in range(31)[::-1]:
		j = i
		xpos = 0
		while(j >= 0):
			xpos += j
			j-= 1
			if(xpos > ts[0][1]):
				break
			elif(xpos >= ts[0][0] and xpos <= ts[0][1]):
				# print("xpos",ts[0][0], xpos, ts[0][1])
				xtry.append(i)
				break
	return xtry
def find_target(ts):
	# xvelo, yvelo = 7, 2
	# steps = max(xvelo, yvelo)
	xtrys = get_xtry(ts)		
	print(xtrys)
	maxypos_list = []
	for xtry in xtrys:
		for ytry in range(1000):
			xpos, ypos = 0, 0
			maxypos = 0
			xvelo, yvelo = xtry, ytry
			while(xpos <= ts[0][1] and ypos >= ts[1][0]):
				
				xpos += xvelo
				ypos += yvelo
				if(xvelo > 0):
					xvelo -= 1
				elif(xvelo < 0):
					xvelo += 1
				yvelo -= 1
				if(maxypos < ypos):
					maxypos = ypos
				if(xpos <= ts[0][1] and xpos >=ts[0][0] and ypos <= ts[1][1] and ypos >=ts[1][0]):
					print("result", xtry, ytry, xpos, ypos, maxypos)
					maxypos_list.append(maxypos)
					# break
	print(maxypos_list)
	print(max(maxypos_list))
find_target(ts)

