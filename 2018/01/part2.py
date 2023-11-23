import time
freq = []
frequency = 0
flag = False
with open("input.txt", "r") as file:
    while flag == False:
        print("it")
        while line := file.readline():
            frequency += int(line.strip())
            for e in freq:
                if e == frequency:
                    flag = True
                    break
            time.sleep(0.001)
        if flag == True:
            break        
        freq.append(frequency)
print(frequency)