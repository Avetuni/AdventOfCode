sum = 0
input = [] #2d arr, first coordinate is line, second character in line

def checkPath(arr, line, col, hori, verti): #line index to start at; character index to start at; direction flags (True up/right; None neutral(at most one neutral); False down/left)
    for i in range(4):

        if line < 0 or col < 0 or line >= len(arr) or col >= len(arr[line]):
            return False
        
        match i:
            case 0: 
                if arr[line][col] != "X":
                    return False
            case 1: 
                if arr[line][col] != "M":
                    return False
            case 2: 
                if arr[line][col] != "A":
                    return False
            case 3: 
                if arr[line][col] != "S":
                    return False
        if hori:
            line +=1
        elif hori == False:
            line -= 1
        if verti:
            col +=1
        elif verti == False:
            col -= 1
    return True

with open("2024\\04\\input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        input.append(list(line.strip()))

rows = len(input)
for line in range(rows):
        cols = len(input[line])
        for col in range(cols):
            if checkPath(input, line, col, hori=None, verti=True): # Upward
                sum += 1
            if checkPath(input, line, col, hori=None, verti=False): # Downward
              sum += 1
            if checkPath(input, line, col, hori=False, verti=None): # Leftward
                sum += 1
            if checkPath(input, line, col, hori=True, verti=None): # Rightward
                sum += 1
            if checkPath(input, line, col, hori=True, verti=True): # Up-right
                sum += 1
            if checkPath(input, line, col, hori=False, verti=True): # Up-left
                sum += 1
            if checkPath(input, line, col, hori=True, verti=False): # Down-right
                sum += 1
            if checkPath(input, line, col, hori=False, verti=False): # Down-left
                sum += 1
print(sum)