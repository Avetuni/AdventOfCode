dinput = []
i = 1
pinput = []
with open("input.txt", "r") as file:
    while line := file.readline().strip():
        dinput.append(int(line))
print("test1")
while i < (len(dinput)-1):
    pinput.append(dinput[i-1] + dinput[i] + dinput[i+1])
    i += 1
print("test2")
previous = 0
current = 0
increases = 0
for e in pinput:
    current = e
    if current > previous:
        increases += 1
    previous = current
print(increases - 1)