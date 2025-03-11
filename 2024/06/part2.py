import itertools
result = 0
def permutations(length):
    return [''.join(p) for p in itertools.product(["+", "*", "|"], repeat=length)]

with open("input.txt", "r") as file:
    while line := file.readline().strip():
        if ":" not in line:
            break
        line = line.split(":")
        line[1] = line[1].strip().split(" ")
        perms = permutations(len(line[1]))
        for i in perms:
            operators = list(i)
            res = 0
            for j in range(len(line[1])):
                if j != 0:
                    if operators[j-1] == "+":
                        res += int(line[1][j])
                    elif operators[j-1] == "*":
                        res *= int(line[1][j])
                    else:
                        res = int(str(res)+line[1][j])
                else:
                    res = int(line[1][j])
            if res == int(line[0]):
                result += int(line[0])
                print(int(line[0]))
                break
                
                
print(result)
