lines = []

with open("input.txt", "r") as file:
    for line in file:
        lines.append(int(line.strip()))

result = 0

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[i] + lines[j] == 2020:
            result = lines[i] * lines[j]
            print(result)
            print(lines[i])
            print(lines[j])
            print("")

print(result)
