with open("input.txt", "r") as file:
    while line := file.readline():
        split = list(line)
        print(split)
floor = 0
basementfloor = 0
flag = False
i = 0
for e in split:
    if e == '(':
        floor += 1
    elif e == ')':
        floor -= 1
    if floor < 0:
        if flag == False:
            basementfloor = i
            flag = True
        print(i)
        print(floor)
    i += 1
print(basementfloor)
print(floor)