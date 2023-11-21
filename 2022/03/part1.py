def getPriority(char):
    if not char:
        return 0
    if char.isupper():
        priority = int(char, 36) - 9 + 26
    else:
        priority = int(char, 36) - 9
    return priority

tester = []
sum = 0
with open("input.txt", "r") as file:
    while line := file.readline():
        first, second = line[:len(line)//2], line[len(line)//2:]
        tester = []
        for e in first:
            ep = getPriority(e.strip())
            for p in second:
                pp = getPriority(p.strip())
                if ep == pp:
                    if ep not in tester:
                        tester.append(ep)
                        sum += ep
                    break

                    

print(sum)
