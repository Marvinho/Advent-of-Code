with open("day9.txt") as f:
	##rules = f.read().rstrip()
	lines = [int(line.rstrip()) for line in f]
print(lines)

def part1(lines, preambel_len):
	i = 0
	result = 0
	while(i+preambel_len < len(lines)):
		arr = lines[i:i+preambel_len]
		sums = []
		for idx, j in enumerate(arr):
			for k in range(idx+1, len(arr)):
				sums.append(j+arr[k])
		#print(sums)
		if(lines[i+preambel_len] not in sums):
			print(lines[i+preambel_len])
			return lines[i+preambel_len]
		i+=1
	return result


inv_number = part1(lines, preambel_len=25)

def part2(lines, inv_number):
	i = 0
	while(i < len(lines)):
		result = 0
		j = 1
		while(inv_number >  result):
			result = sum(lines[i:j])
			if(result == inv_number):
				print("INV NUMBER", lines[i:j])
				enc_weakness = min(lines[i:j]) + max(lines[i:j])
				print("RESULT:" ,min(lines[i:j]) + max(lines[i:j]))
				return enc_weakness
			j+=1
		print(result)
		i+=1
part2(lines, inv_number)