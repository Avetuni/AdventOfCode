previous = 0
current = 0
increases = 0

with open("input.txt", "r") as file:
    while line := file.readline():
        current = int(line)
        if current > previous:
            increases += 1
        previous = current
print(increases - 1)