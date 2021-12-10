with open("day10.txt") as f:
	lines = []
	for c in f:
		lines.append(c.strip())

print(lines)

def first_illegal_character(lines):
	ill_list = []
	for line in lines:
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
							break
					case "]":
						if(stack[-1] == "["):
							stack.pop()
						else:
							ill_list.append(bracket)
							break
					case "}":
						if(stack[-1] == "{"):
							stack.pop()
						else:
							ill_list.append(bracket)
							break
					case ">":
						if(stack[-1] == "<"):
							stack.pop()
						else:
							ill_list.append(bracket)
							break
	print(ill_list)
	return ill_list

def calc_score(ill_list):
	score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
	score = 0
	for ill in ill_list:
		score += score_dict[ill]
	print(score)
	return score



ill_list = first_illegal_character(lines)
calc_score(ill_list)