# import numpy as np
# with open("test.txt") as f:
# 	lines = [line.rstrip().replace(" ", "") for line in f]
#print(lines)

# def part1(lines):
# 	for line in lines[:1]:
# 		openbr = 0
# 		rem = 0
# 		i = 0
# 		arr = []
# 		while(i < len(line)):
# 			if(openbr == 0 and line[i] == "("):
# 				arr.append(line[rem:i])
# 				openbr +=1
# 				rem = i
# 			elif(line[i] == "("):
# 				openbr += 1
# 			elif(line[i] == ")"):
# 				openbr -= 1
# 				if(openbr == 0):
# 					arr.append(line[rem:i+1])
# 					rem = i+1

# 			i+=1
# 			print(arr)

# a = lines[0]
# a = [i for i in a]
# def reduce(eq):
# 	if(len(eq) == 1):
# 		return eq[0]
# 	while(len(eq) > 1):

# 		arr = []
# 		c = eq.pop(0) 
# 		elif(c in "0123456789+*"):
# 			arr.append(c)
# 		elif(c in "("):
# 			reduce(eq)
# 		elif(c in ")"):
# 			return arr

# reduce(a)		

class T:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return T(self.v + other.v)
    def __sub__(self, other):
        return T(self.v * other.v)
    def __mul__(self, other):
        return T(self.v + other.v)

def main():
    part2 = True
    with open("day18.txt") as f:
        inp = f.read()
    # with open("example_input.txt") as f:
    #     inp = f.read()

    lines = [line for line in inp.split("\n") if line]
    t = 0
    for line in lines:
        for d in range(10):
            line = line.replace(f"{d}", f"T({d})")
        line = line.replace("*", "-")
        if part2:
            line = line.replace("+", "*")
        t += eval(line, {"T": T}).v
    print(t)

if __name__ == '__main__':
    main()

