with open("day16.txt") as f:
	arr = []
	for line in f:
		arr.append(line.strip())
	# print(arr)

global version_score
version_score = 0
def decode(bitstr, parse_idx=0):
	global version_score
	if(len(bitstr)<11):
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
		bitstr, numberstr, add_idx = literal_value(bitstr)
		parse_idx+= add_idx
		print("RETURNING", bitstr, numberstr, parse_idx)
		return bitstr, numberstr, parse_idx
	else:
		bitstr, numberstr, parse_idx = operator(bitstr)
		return bitstr, numberstr, parse_idx

def operator(bitstr):
	# print(bitstr)
	lentype_id = bitstr[0]
	bitstr = bitstr[1:]
	print("lentype", lentype_id)
	parse_idx = 0
	if(lentype_id == "0"):
		shiftby = 15
		len_of_subpackets_in_bits = bitstr[:shiftby]
		len_of_subpackets_in_bits = int(len_of_subpackets_in_bits, 2)
		print("len_of_subpackets_in_bits", len_of_subpackets_in_bits)
		print(bitstr[shiftby:])
		bitstr = bitstr[shiftby:]
		
		while(parse_idx < len_of_subpackets_in_bits):
			print(bitstr, parse_idx)
			# bitstr = bitstr[parse_idx:]
			# print(bitstr)
			bitstr, numberstr, add_idx = decode(bitstr, parse_idx)
			parse_idx = add_idx
			print("parse_idx", parse_idx)
		return bitstr, numberstr, add_idx
	elif(lentype_id == "1"):
		print(bitstr)
		shiftby = 11
		num_of_subs_contained = bitstr[:shiftby]
		num_of_subs_contained = int(num_of_subs_contained, 2)
		bitstr = bitstr[shiftby:]
		print("NUM OF SUBS CONTAINED", num_of_subs_contained)
		for i in range(0, num_of_subs_contained):
			# print("bitstr, i ", bitstr, i)
			bitstr, _, parse_idx = decode(bitstr, parse_idx)
		print("returning", bitstr)
		return bitstr, 0, parse_idx

def literal_value(bitstr):
	# print("lit value bitstr", bitstr)
	# print(type(bitstr))
	startbit = 1
	add_idx = 0
	# print("startbit", startbit)
	numberstr = ""
	while(startbit != "0"):
		numberstr += bitstr[1:5]
		startbit = bitstr[0]
		bitstr = bitstr[5:]
		# print(bitstr, startbit, numberstr)
		add_idx+=5
	# print(numberstr)
	numberstr = int(numberstr, 2)
	print("LITERAL VALUE", numberstr)
	# print("bitstr", bitstr)
	return bitstr, numberstr, add_idx


if __name__ == '__main__':
	for ar in arr[:1]:
		print(ar)
		bitstr = ""
		for ch in ar:
			ch = f'{int(ch, 16):b}'
			while(len(ch)< 4):
				ch = "0" + ch
			bitstr+=ch
		decode(bitstr)
		print("VERSION_SCORE", version_score)