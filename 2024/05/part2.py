import copy

ogmap = []
with open("input.txt", "r") as file:
    while line := file.readline():
        ogmap.append(list(line.strip()))

def pathfind(map):
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
                    return True
                else:
                    if map[coordinates[0] - 1][coordinates[1]] == "#":
                        direction = "e"
                    else:
                        coordinates[0] -= 1

            case "e":
                if coordinates[1] == len(map[0]) - 1:
                    return True
                else:
                    if map[coordinates[0]][coordinates[1] + 1] == "#":
                        direction = "s"
                    else:
                        coordinates[1] += 1

            case "s":
                if coordinates[0] == len(map) - 1:
                    return True
                else:
                    if map[coordinates[0] + 1][coordinates[1]] == "#":
                        direction = "w"
                    else:
                        coordinates[0] += 1

            case "w":
                if coordinates[1] == 0:
                    return True
                else:
                    if map[coordinates[0]][coordinates[1] - 1] == "#":
                        direction = "n"
                    else:
                        coordinates[1] -= 1
    return False

result = 0
for i in range(len(ogmap)):
    for j in range(len(ogmap[i])):
        amap = copy.deepcopy(ogmap)
        if amap[i][j] not in ["^", "<", ">", "v"]:
            amap[i][j] = "#"
            if not pathfind(amap):
                result += 1
                print(i, j)


print(result)
