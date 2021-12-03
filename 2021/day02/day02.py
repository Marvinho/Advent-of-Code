with open("day02.txt") as f:
    commands = []
    for line in f:
        line = line.rstrip().split(" ")
        line[1] = int(line[1])
        commands.append(line)
print(commands)

def calc_position_part1(commands):
    pos = [0, 0] # x,y
    for command, i in commands:
        if(command == "forward"):
            pos[0] += i
        elif(command == "up"):
            pos[1] -= i
        elif(command=="down"):
            pos[1] += i
    return pos

part1res = calc_position_part1(commands)
print(part1res[0]*part1res[1])

def calc_position_part2(commands):
    pos = [0, 0, 0] # x,y,aim
    for command, i in commands:
        if(command == "down"):
            pos[2]+= i
        if(command == "up"):
            pos[2]-= i
        if(command == "forward"):
            pos[0]+=i
            pos[1] += pos[2]*i
    return pos
pos = calc_position_part2(commands)
print(pos[0]*pos[1])
