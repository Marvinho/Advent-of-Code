with open("day02.txt") as f:
    commands = []
    for line in f:
        line = line.rstrip().split(" ")
        line[1] = int(line[1])
        commands.append(line)
print(commands)

def calc_position(commands):
    pos = [0, 0]
    for command, i in commands:
        if(command == "forward"):
            pos[0] += i
        elif(command == "up"):
            pos[1] -= i
        elif(command=="down"):
            pos[1] += i
    return pos

part1res = calc_position(commands)
print(part1res[0]*part1res[1])