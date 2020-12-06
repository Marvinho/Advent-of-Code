with open("day6_input.txt") as f:
	a = f.read().strip().split("\n\n")
	b = [x.replace("\n"," ") for x in a]
	#lines = [line.rstrip() for line in f]
print(b)

form_set = "abcdefghijklmnopqrstuvwxyz"
def customCustoms(b):
	result = 0
	for i in b:
		yes = ""
		for j in i:
			if(j in form_set):
				if(j not in yes):
					yes+=j
					result+=1
	return result
result = customCustoms(b)
#print(result)

def part2(b):
	result = 0
	for i in b:
		groups = i.split(" ")
		i = i.replace(" ","")
		answers = {}
		for char in i:
			if(char in answers):
				answers[char] += 1
			else:
				answers[char] = 1
		
		num_groups = len(groups)
		for k, v in answers.items():
			if(v == num_groups):
				result+=1
		#print(num_groups, answers)

	return result

result = part2(b)
print(result)