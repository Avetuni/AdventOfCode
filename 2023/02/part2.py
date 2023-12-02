total = 0
maxr = 12
maxg = 13
maxb = 14
color_dict = {'blue': 0, 'red': 0, 'green': 0}
with open("input.txt", "r") as file:
    while line := file.readline().replace(":", "").replace(",", "").replace("Game ", "").replace(";" , "").replace("\n", "").split(" "):
        color_dict["blue"] = 0
        color_dict["green"] = 0
        color_dict["red"] = 0
        for i in range(len(line) - 1):
            if line[i+1].isdigit():
                value = int(line[i+1])
                color = line[i + 2]
                print(color + str(value))
                if color_dict[color] < value:
                    color_dict[color]= value
        total += color_dict["blue"] * color_dict["green"] * color_dict["red"]
        
        if int(line[0]) > 99:
            break

print(total)
