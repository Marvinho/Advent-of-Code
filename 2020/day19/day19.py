import numpy as np
with open("test.txt") as f:
	lines = [line.rstrip() for line in f]
print(lines)

rules_num = 6
rules = lines[:rules_num]
messages = lines[rules_num+1:]
print(rules)

rule_dict = {}
for rule in rules:
	all_pattern = []
	rule_id, pattern = rule.split(": ")
	print(rule_id, pattern)
	if('"' in pattern):
		all_pattern = pattern.strip(" ").replace('"',"")
	else:
		if("|" in pattern):
			pattern = pattern.strip(" ").split("|")
		for pat in pattern:
			try:
				all_pattern.append(list(map(int, pat.strip(" ").split(" "))))
			except:
				pass
	rule_dict[int(rule_id)] = all_pattern

print(rule_dict)
print(messages)

temp_rule = []
while(rule_dict[0] != temp_rule):
	temp_rule = rule_dict[0]
	for idx, rule in enumerate(rule_dict[0]):
		for jdx, r in enumerate(rule):
			rule[0][idx][jdx] =  rule_dict[r]
	print(rule_dict[0])

	