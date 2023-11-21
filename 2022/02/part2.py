score = 0
with open("input.txt", "r") as file:
    while line := file.readline():
        split = line.split()
        if split[1] == "X":
            if split[0] == "A":
                score += 3
            elif split[0] == "B":
                score += 1
            else:
                score += 2
        elif split[1] == "Y":
            score += 3
            if split[0] == "A":
                score += 1
            elif split[0] == "B":
                score += 2
            else:
                score += 3
        else:
            score += 6
            if split[0] == "A":
                score += 2
            elif split[0] == "B":
                score += 3
            else:
                score += 1
print(score)
