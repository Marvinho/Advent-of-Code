import copy
from collections import defaultdict
with open("day22.txt") as f:
	lines = [line.rstrip() for line in f]
# print(lines)
def parse_input(lines):
	card_decks = defaultdict(list)
	player = 0
	for line in lines:
		if("Player" in line):
			player+=1
		elif(len(line) > 0):
			card_decks[player].append(int(line))
	# print(card_decks)
	return card_decks

card_decks = parse_input(lines)
deck1 = card_decks[1]
deck2 = card_decks[2]

def part1(deck1, deck2):
	while(deck1 and deck2):
		a = deck1.pop(0)
		b = deck2.pop(0)
		if(a > b):
			deck1.extend([a, b])
		else:
			deck2.extend([b, a])
		print(deck1, deck2)
	if(deck1):
		return deck1
	else:
		return deck2


def part2(deck1, deck2):
	seen = set()
	deck1 = deck1.copy()
	deck2 = deck2.copy()
	
	while(deck1 and deck2):
		round_played = str((deck1, deck2))
		if(round_played in seen):
			# print(deck1)
			return 1, deck1
		else:
			seen.add(round_played)

		a = deck1.pop(0)
		b = deck2.pop(0)

		if(a <= len(deck1) and b <= len(deck2)):
			winner, _ = part2(deck1[:a], deck2[:b])
			if(winner == 1):
				deck1.extend([a, b])
			elif(winner == 2):
				deck2.extend([b, a])
			else:
				return 0, deck1, deck2
		else:
			if(a > b):
				deck1.extend([a, b])
			elif(b > a):
				deck2.extend([b, a])
			else:
				return 0,deck1,deck2
	if(deck1):
		return 1, deck1
	else:
		return 2, deck2

def calc_score(winner_deck):
	result = 0
	for idx, i in enumerate(reversed(winner_deck)):
		result += (idx+1) * i
	print(result)

winner, winner_deck = part2(deck1, deck2)
print(winner_deck)
calc_score(winner_deck)
calc_score(deck1)
