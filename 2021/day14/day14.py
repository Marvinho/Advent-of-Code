import re
from collections import Counter
with open("day14.txt") as f: 
	rules = {}
	for line in f:
		line = line.strip()
		
		if(not line):
			continue
		if("->" in line):
			line = line.split(" -> ")
			rules[line[0]] = line[1]
		else:
			polymer = line
		

print(polymer, rules)

def insert(polymer, rules, num=40):
	print(polymer, rules)
	

	for i in range(num):
		inserts = [None]*len(polymer)
		for key, value in rules.items():
			# print(key, value)
			if(key in polymer):
				# print(key)
				asdf = [match.start()+1 for match in re.finditer('(?={})'.format(key), polymer)]
				# print(key, asdf)
				for a in asdf:
					inserts[a] = value
				# inserts.append(value)
		# print(inserts)
		for pos, ins in enumerate(inserts[::-1]):
			if(ins is None):
				continue
			else:
				at = len(inserts)-pos-1
				polymer = polymer[:at] + ins + polymer[at:]
		# print(polymer)
		cnter = Counter(polymer)
		score = max(cnter.values())-min(cnter.values())
		print(score)


if __name__ == '__main__':
	insert(polymer, rules)