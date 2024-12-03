import re

sum = 0
matches = []

with open("input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        for i in matches:
            sum += int(i[0]) * int(i[1])


print(sum)
