import re

sum = 0
matches = []
curInstruction = True

with open("2024\\03\\input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        matches = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))", line)
        for i in matches:
            if i[0]:
                if curInstruction:
                    sum += int(i[1]) * int(i[2])
            elif i[3]:
                curInstruction = True
            elif i[4]:
                curInstruction = False


print(sum)
