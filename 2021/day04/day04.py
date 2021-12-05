import numpy as np

with open("day04.txt") as f:
    bingo_cards = []
    bingo_card = np.full((7,7), -1, dtype=int)
    counter = 0
    row = 0
    for i, line  in enumerate(f):
        if(i==0):
            number_draws = [int(x) for x in line.rstrip().split(",")]
        else:

            line = [int(x) for x in line.rstrip().split()]
            if(not line):
                counter+=1
                # print(counter)
                
                bingo_card = np.full((7,7), -1, dtype=int)
                row = 0
            else:
                # print(line)

                bingo_card[row, 0:5] = line
                row+=1
                if(row == 5):
                    bingo_cards.append(bingo_card)


            # print(not line)
            # bingo_card
            # np.append(bingo_cards, line)

def play_bingo(bingo_cards, number_draws):
    for number in number_draws:
        # print(number)
        for bingo_card in bingo_cards:
            for row in bingo_card:
                if(number in row[:5]):
                    x, y = np.where(bingo_card[:5,:5]==number)
                    x, y = x[0], y[0]
                    bingo_card[x][5] -= 1
                    bingo_card[5][y] -= 1
                    bingo_card[6][6]-= number
            if((-6 in bingo_card[5,0:5]) or (-6 in bingo_card[0:5,5])):
                return bingo_card, number
        # print(bingo_cards)

# winner_card, winner_nr = play_bingo(bingo_cards, number_draws)
# print(winner_card, winner_nr)

def calc_score(winner_card, winner_nr):
    # print(winner_card[6][6] +1)
    score = np.sum(winner_card[:5,:5]) + winner_card[6][6] +1
    score *= winner_nr
    return score

# score = calc_score(winner_card, winner_nr)
# print(score)

def play_bingo_part2(bingo_cards, number_draws):
    print(len(bingo_cards))
    nr_of_winners = 0
    for number in number_draws:
        # print(number)
        for bingo_card in bingo_cards:

            for row in bingo_card:
                if(number in row[:5]):
                    x, y = np.where(bingo_card[:5,:5]==number)
                    x, y = x[0], y[0]
                    bingo_card[x][5] -= 1
                    bingo_card[5][y] -= 1
                    bingo_card[6][6]-= number
            if((-6 in bingo_card[5,0:5]) or (-6 in bingo_card[0:5,5])):
                if(len(bingo_cards)-1==nr_of_winners):
                    print("all card:",bingo_cards, number)
                    return bingo_card, number
                else:
                    bingo_card[:,:] = 999999
                    print(bingo_card)
                    nr_of_winners+=1

winner_card, winner_nr = play_bingo_part2(bingo_cards, number_draws)
print(winner_card, winner_nr)
score = calc_score(winner_card, winner_nr)
print(score)