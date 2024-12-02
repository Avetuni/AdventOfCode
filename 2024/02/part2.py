sum = 0
dirFlag = None #true asc, false desc
tempArr = []
def checkValid(splitLine):
    if int(splitLine[0]) < int(splitLine[1]):
        dirFlag = True
    else:
        dirFlag = False
    for i in range(len(splitLine)):
        if i != len(splitLine)-1:
            if dirFlag:
                if int(splitLine[i+1]) - int(splitLine[i]) < 1 or int(splitLine[i+1]) - int(splitLine[i]) > 3:
                    return False
            else:
                if int(splitLine[i]) - int(splitLine[i+1]) < 1 or int(splitLine[i]) - int(splitLine[i+1]) > 3:
                    return False
    return True



with open("2024\\02\\input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        splitLine = line.strip().split(" ")

        if checkValid(splitLine):
            sum += 1
        else:
            for i in range(len(splitLine)):
                tempArr = splitLine[:i] + splitLine[i+1:]
                if checkValid(tempArr):
                    sum += 1
                    break
print(sum)

