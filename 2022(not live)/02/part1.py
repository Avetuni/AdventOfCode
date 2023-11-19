score = 0
with open("input.txt", "r") as file:
    while line := file.readline():
        split = line.split()
        if split[1] == "Z":
            score += 3
            if split[0] == "B":
                score += 6
            elif split[0] == "C":
                score += 3
        elif split[1] == "Y":
            score += 2
            if split[0] == "A":
                score += 6
            elif split[0] == "B":
                score += 3
        else:
            score += 1
            if split[0] == "A":
                score += 3
            elif split[0] == "C":
                score += 6
print(score)
