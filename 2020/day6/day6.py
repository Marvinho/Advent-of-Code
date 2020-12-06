with open("test.txt") as f:
	a = f.read().strip().split("\n\n")
	all_answers = [x.replace("\n","") for x in a]
	#lines = [line.rstrip() for line in f]
print(all_answers)

form_set = "abcdefghijklmnopqrstuvwxyz"
def customCustoms(all_answers):
	result = 0
	for group_answers in all_answers:
		set_answers = set("".join(group_answers))
		result+=len(set_answers)
	return result
result = customCustoms(all_answers)
print(result)

# def part2(b):
# 	result = 0
# 	for i in b:
# 		groups = i.split(" ")
# 		i = i.replace(" ","")
# 		answers = {}
# 		for char in i:
# 			if(char in answers):
# 				answers[char] += 1
# 			else:
# 				answers[char] = 1
		
# 		num_groups = len(groups)
# 		for k, v in answers.items():
# 			if(v == num_groups):
# 				result+=1
# 		#print(num_groups, answers)

# 	return result

# result = part2(b)
# print(result)