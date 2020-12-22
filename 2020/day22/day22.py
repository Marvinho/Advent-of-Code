from collections import defaultdict
with open("day22.txt") as f:
	lines = [line.rstrip() for line in f]
print(lines)
def parse_input(lines):
	card_decks = defaultdict(list)
	player = 0
	for line in lines:
		if("Player" in line):
			player+=1
		elif(len(line) > 0):
			card_decks[player].append(int(line))
	print(card_decks)
	return card_decks

card_decks = parse_input(lines)

def part1(card_decks):
	deck1 = card_decks[1]
	deck2 = card_decks[2]
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


winner_deck = part1(card_decks)
def calc_score(winner_deck):
	result = 0
	for idx, i in enumerate(reversed(winner_deck)):
		result += (idx+1) * i
	print(result)

calc_score(winner_deck)