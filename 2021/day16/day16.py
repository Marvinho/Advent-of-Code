with open("testday16-2.txt") as f:
	arr = []
	for line in f:
		arr.append(line.strip())
	# print(arr)

global version_score
version_score = 0

def decode(bitstr, parse_idx=0):
	numberstr = []
	global version_score
	if(len(bitstr)<6):
		print(version_score)
		exit()
	vers = bitstr[:3]
	vers = int(vers, 2)
	typeid = bitstr[3:6]
	typeid = int(typeid, 2)
	parse_idx+=6
	
	version_score+= vers
	print("Version: {}, Typeid: {}".format(vers, typeid))
	bitstr = bitstr[6:]
	if(typeid == 4):
		bitstr, numberstr, add_idx = literal_value(bitstr, numberstr)
		parse_idx+= add_idx
		return bitstr, numberstr, parse_idx
	elif(typeid==0):
		bitstr, num, parse_idx = operator(bitstr, numberstr)
		numberstr = num
		numberstr = [sum(numberstr)]
		print("sum",numberstr)
		return bitstr, numberstr, parse_idx
	elif(typeid==1):
		bitstr, num, parse_idx = operator(bitstr, numberstr)
		numberstr = num
		result = 1
		for x in numberstr:
			result = result*x
		
		numberstr = [result]
		print("mult",numberstr)
		print(bitstr, numberstr, parse_idx)
		return bitstr, numberstr, parse_idx
	elif(typeid==2):
		bitstr, numberstr, parse_idx = operator(bitstr, numberstr)
		numberstr = [min(numberstr)]
		print("min",numberstr)
		return bitstr, numberstr, parse_idx	
	elif(typeid==3):
		bitstr, numberstr, parse_idx = operator(bitstr, numberstr)
		numberstr = [max(numberstr)]
		print("max",numberstr)
		return bitstr, numberstr, parse_idx	
	elif(typeid==5):
		bitstr, numberstr, parse_idx = operator(bitstr, numberstr)
		if(numberstr[0] > numberstr[1]):
			numberstr = [1]
		else:
			numberstr = [0]
		print("greaterthan",numberstr)
		return bitstr, numberstr, parse_idx	
	elif(typeid==6):
		bitstr, numberstr, parse_idx = operator(bitstr, numberstr)
		if(numberstr[0] < numberstr[1]):
			numberstr = [1]
		else:
			numberstr = [0]
		print("lessthan",numberstr)
		return bitstr, numberstr, parse_idx
	elif(typeid==7):
		bitstr, numberstr, parse_idx = operator(bitstr, numberstr)
		print(bitstr, numberstr, parse_idx)
		print("equal",numberstr)
		if(numberstr[0] == numberstr[1]):
			numberstr = [1]
		else:
			numberstr = [0]
		# print("WWWWWWWWWWWWWWWWWWW",numberstr)
		return bitstr, numberstr, parse_idx
	# else:
		# bitstr, numberstr, parse_idx = operator(bitstr, numberstr)
		# return bitstr, numberstr, parse_idx
def operator(bitstr, numberstr):
	# print(bitstr)
	lentype_id = bitstr[0]
	bitstr = bitstr[1:]
	# print("lentype", lentype_id)
	parse_idx = 0
	if(lentype_id == "0"):
		shiftby = 15
		len_of_subpackets_in_bits = bitstr[:shiftby]
		len_of_subpackets_in_bits = int(len_of_subpackets_in_bits, 2)
		bitstr = bitstr[shiftby:]		
		while(parse_idx < len_of_subpackets_in_bits):
			bitstr, numstr, add_idx = decode(bitstr, parse_idx)
			numberstr.extend(numstr)
			parse_idx = add_idx
		return bitstr, numberstr, add_idx
	elif(lentype_id == "1"):
		shiftby = 11
		num_of_subs_contained = bitstr[:shiftby]
		num_of_subs_contained = int(num_of_subs_contained, 2)
		bitstr = bitstr[shiftby:]
		# print("NUM OF SUBS CONTAINED", num_of_subs_contained)
		for i in range(0, num_of_subs_contained):
			bitstr, numstr, parse_idx = decode(bitstr, parse_idx)
			numberstr.extend(numstr)
		return bitstr, numberstr, parse_idx

def literal_value(bitstr, numberstr):
	startbit = 1
	add_idx = 0
	numstr = ""
	while(startbit != "0"):
		numstr += bitstr[1:5]
		startbit = bitstr[0]
		bitstr = bitstr[5:]
		add_idx+=5
	numberstr = [int(numstr, 2)]
	print("LITERAL VALUE", numberstr)
	print(bitstr, numberstr, add_idx)
	return bitstr, numberstr, add_idx


if __name__ == '__main__':
	for ar in arr[:8]:
		print(ar)
		bitstr = ""
		for ch in ar:
			ch = f'{int(ch, 16):b}'
			while(len(ch)< 4):
				ch = "0" + ch
			bitstr+=ch
		decode(bitstr)
		print("VERSION_SCORE", version_score)