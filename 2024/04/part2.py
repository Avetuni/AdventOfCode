sum = 0
input = [] #2d arr, first coordinate is line, second character in line

with open("2024\\04\\input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        input.append(list(line.strip()))

rows = len(input)
for line in range(1, rows-1):
    cols = len(input[line])
    for col in range(1, cols-1):
        if input[line][col] == "A":
            if {input[line+1][col-1], input[line-1][col+1]} == {"M", "S"} and {input[line-1][col-1], input[line+1][col+1]} == {"M", "S"}:
                sum += 1

print(sum)