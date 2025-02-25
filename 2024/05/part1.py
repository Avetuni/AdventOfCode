map = []
with open("input .txt", "r") as file:
    while line := file.readline():
        map.append(list(line.strip()))


direction = ""
coordinates = [0,0]
for i in range(len(map)):
    if "^" in map[i]:
        coordinates = [i, map[i].index("^")]
        direction = "n"
        break
    if ">" in map[i]:
        coordinates = [i, map[i].index(">")]
        direction = "e"
        break
    if "<" in map[i]:
        coordinates = [i, map[i].index("<")]
        direction = "w"
        break
    if "v" in map[i]:
        coordinates = [i, map[i].index("v")]
        direction = "s"
        break
for i in range(10000):
    match direction:
        case "n":
            if coordinates[0] == 0:
                map[coordinates[0]][coordinates[1]] = "X"
                break
            else:
                if map[coordinates[0] - 1][coordinates[1]] == "#":
                    direction = "e"
                else:
                    map[coordinates[0]][coordinates[1]] = "X"
                    coordinates[0] -= 1

        case "e":
            if coordinates[1] == len(map[0]) - 1:
                map[coordinates[0]][coordinates[1]] = "X"
                break
            else:
                if map[coordinates[0]][coordinates[1] + 1] == "#":
                    direction = "s"
                else:
                    map[coordinates[0]][coordinates[1]] = "X"
                    coordinates[1] += 1
        case "s":
            if coordinates[0] == len(map) - 1:
                map[coordinates[0]][coordinates[1]] = "X"
                break
            else:
                if map[coordinates[0] + 1][coordinates[1]] == "#":
                    direction = "w"
                else:
                    map[coordinates[0]][coordinates[1]] = "X"
                    coordinates[0] += 1
        case "w":
            if coordinates[1] == 0:
                map[coordinates[0]][coordinates[1]] = "X"
                break
            else:
                if map[coordinates[0]][coordinates[1] - 1] == "#":
                    direction = "n"
                else:
                    map[coordinates[0]][coordinates[1]] = "X"
                    coordinates[1] -= 1

result = 0
for i in map:
    result += i.count("X")
print(result)
