with open("input.txt", "r") as file:
    while line := file.readline():
        if line == "\n":
            break
        lines = line.split(" ")
        for e in lines:
            print(e.strip().replace("[", "").replace("]", ""))