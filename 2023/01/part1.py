total = 0
with open("input.txt", "r") as file:
    while line := list(file.readline()):
        for e in line:
            if e.isdigit():
                total += int(e) * 10
                break
        
        for e in reversed(line):
            if e.isdigit():
                total += int(e)
                break
print(total)