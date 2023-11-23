frequency = 0
with open("input.txt", "r") as file:
    while line := file.readline():
        frequency += int(line.strip())
print(frequency)