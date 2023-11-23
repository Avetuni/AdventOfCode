horizontal = 0
depth = 0

with open("input.txt", "r") as file:
    while line := file.readline().strip():
        command = line.split(" ")[0].strip()
        number = int(line.split(" ")[1].strip())
        if command == "forward":
            horizontal += number
        elif command == "down":
            depth -= number
        else:
            depth += number

print(depth*horizontal)