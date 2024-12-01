sum = 0
arr1 = []
arr2 = []

with open("2024\\01\\input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        split_line = line.strip().split("   ")
        if len(split_line) >= 2:
            arr1.append(int(split_line[0]))
            arr2.append(int(split_line[1]))
arr1.sort()
arr2.sort()

for i in arr1:
    numToCheck = i
    for j in arr2:
        if j == i:
            sum += i

print(sum)
