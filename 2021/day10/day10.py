with open("day10.txt") as f:
	lines = []
	for c in f:
		lines.append(c.strip())

# print(lines)

def first_illegal_character(lines):
	score_auto_dict = {"(":1, "[":2, "{":3, "<":4}
	score = 0
	scores = []
	ill_list = []
	incompletes = []
	for line in lines:
		flag = True
		stack = [line[0]]
		for bracket in line[1:]:
			if(bracket in "(<{["):
				stack.append(bracket)
			else:
				match bracket:
					case ")":
						if(stack[-1] == "("):
							stack.pop()
						else:
							ill_list.append(bracket)
							flag = False
							break
					case "]":
						if(stack[-1] == "["):
							stack.pop()
						else:
							ill_list.append(bracket)
							flag = False
							break
					case "}":
						if(stack[-1] == "{"):
							stack.pop()
						else:
							ill_list.append(bracket)
							flag = False
							break
					case ">":
						if(stack[-1] == "<"):
							stack.pop()
						else:
							ill_list.append(bracket)
							flag = False
							break
		if(flag):
			for s in stack[::-1]:
				score = (score*5)+ score_auto_dict[s]			
			scores.append(score)
			score = 0
			incompletes.append(line)
			print(scores)

	# scores = scores.sort()
	scores.sort()
	print(scores)
	print(scores[int(len(scores)/2)])
	return incompletes, ill_list
	

def calc_score_part1(ill_list):
	score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
	score = 0
	for ill in ill_list:
		score += score_dict[ill]
	print(score)
	return score


incompletes, ill_list = first_illegal_character(lines)