import re
import timeit
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
	freq_of_bigrams = {}
	for key in rules.keys():
		freq_of_bigrams[key] = 0
	for i in range(len(polymer[:-1])):
		bigram = polymer[i]+polymer[i+1]
		if(bigram in freq_of_bigrams):
			freq_of_bigrams[bigram] +=1
	print(freq_of_bigrams)
	for i in range(1, num+1):		
		new_freq_of_bigrams = freq_of_bigrams.copy()
		for rule, insertion in rules.items():
			if(freq_of_bigrams[rule] > 0):
				freq = freq_of_bigrams[rule]
				bigram1 = rule[0]+insertion
				bigram2 = insertion+rule[1]
				new_freq_of_bigrams[bigram1] += freq
				new_freq_of_bigrams[bigram2] += freq
				new_freq_of_bigrams[rule] -= freq
		# print(new_freq_of_bigrams)
		print("step", i, sum(new_freq_of_bigrams.values())+1)
		freq_of_bigrams = new_freq_of_bigrams
	return freq_of_bigrams

def calc_score(polymer, freq_of_bigrams):
	occurrences = {polymer[0]:1, polymer[-1]:1}
	for key, value in freq_of_bigrams.items():
		element1 = key[0]
		element2 = key[1]
		if(element1 not in occurrences):
			occurrences[element1] = value/2
		else:
		 	occurrences[element1] += value/2
		if(element2 not in occurrences):
			occurrences[element2] = value/2
		else:
		 	occurrences[element2] += value/2
	occurrences[polymer[0]]-=0.5
	occurrences[polymer[-1]]-=0.5
	print(occurrences)
	return max(occurrences.values()) - min(occurrences.values())
#############################################################
#represent string as frequencies of bigrams??????????
#############################################################

if __name__ == '__main__':
	freq_of_bigrams = insert(polymer, rules)
	score = calc_score(polymer,freq_of_bigrams)
	print(score)