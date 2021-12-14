import re
import timeit
from collections import Counter
with open("testday14.txt") as f: 
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
		start = timeit.default_timer()
		inserts = [None]*len(polymer)
		for key, value in rules.items():
			if(key in polymer):
				asdf = [match.start()+1 for match in re.finditer('(?={})'.format(key), polymer)]
				for a in asdf:
					inserts[a] = value
		
		poly_arr = list(polymer)
		stop = timeit.default_timer()

		print('1Time: ', stop - start) 
		for pos, ins in enumerate(inserts[::-1]):
			if(ins is None):
				continue
			else:
				at = len(inserts)-pos-1
				poly_arr[at:at] = ins 
		stop = timeit.default_timer()
		print('2Time: ', stop - start) 
		# print(poly_arr)
		polymer = "".join(poly_arr)
		cnter = Counter(polymer)
		score = max(cnter.values())-min(cnter.values())
		# print(score)
		stop = timeit.default_timer()
		print('3Time: ', stop - start) 
#############################################################
#represent string as frequencies of bigrams??????????
#############################################################

if __name__ == '__main__':
	insert(polymer, rules)