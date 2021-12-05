with open("day05.txt") as f:
    line_of_vents = []
    for line in f:
        line = line.replace(" -> ",",")
        line = line.rstrip().split(",")
        line_of_vents.append([int(x) for x in line])
print(line_of_vents)

def find_vents(line_of_vents):
    diagram = [[0 for x in range(1000)] for x in range(1000)]
    # print(diagram)
    for line in line_of_vents:
        x1, y1, x2, y2 = line
        if(x1==x2):
            l = [x for x in range(min(y1,y2), max(y1,y2)+1)]
            for pos in l:
                diagram[x1][pos]+=1
            # print(l)
        elif(y1==y2):
            l = [x for x in range(min(x1,x2), max(x1,x2)+1)]
            # print(l)
            for pos in l:
                diagram[pos][y1]+=1
        elif((x1 > x2) and (y1>y2)):
            xl = [x for x in range(min(x1,x2), max(x1,x2)+1)][::-1]
            yl = [y for y in range(min(y1,y2), max(y1,y2)+1)][::-1]
            for xpos, ypos in zip(xl, yl):
                diagram[xpos][ypos]+=1            
        elif(x1 > x2 and y1 < y2):
            print(x1, y1, x2, y2)
            # print([x for x in range(min(x1,x2), max(x1,x2)+1)][::-1])
            xl = [x for x in range(min(x1,x2), max(x1,x2)+1)][::-1]
            yl = [y for y in range(min(y1,y2), max(y1,y2)+1)]
            # print(xl, yl)
            for xpos, ypos in zip(xl, yl):
                diagram[xpos][ypos]+=1
        elif(y1 > y2):
            xl = [x for x in range(min(x1,x2), max(x1,x2)+1)]
            yl = [y for y in range(min(y1,y2), max(y1,y2)+1)][::-1]
            for xpos, ypos in zip(xl, yl):
                diagram[xpos][ypos]+=1
        else:
            xl = [x for x in range(min(x1,x2), max(x1,x2)+1)]
            yl = [y for y in range(min(y1,y2), max(y1,y2)+1)]
            for xpos, ypos in zip(xl, yl):
                diagram[xpos][ypos]+=1
        # print(diagram)
    return diagram
import numpy as np
diagram = find_vents(line_of_vents)
print(np.array(diagram).T)

def find_vents_part2(line_of_vents):
    diagram = [[0 for x in range(10)] for x in range(10)]
    # print(diagram)
    for line in line_of_vents:
        x1, y1, x2, y2 = line
        xl = [x for x in range(min(x1,x2), max(x1,x2)+1)]
        yl = [y for y in range(min(y1,y2), max(y1,y2)+1)]
        for xpos, ypos in zip(xl, yl):
                diagram[xpos][ypos]+=1
    return diagram
import numpy as np
# diagram = find_vents_part2(line_of_vents)
# print(np.array(diagram).T)

def calc_score(diagram):
    score = 0
    for i in diagram:
        for j in i:
            if(j>=2):
                score+=1
    return score
score = calc_score(diagram)
print(score)