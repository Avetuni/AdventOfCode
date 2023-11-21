def getPriority(char):
    if not char:
        return 0
    if char.isupper():
        priority = int(char, 36) - 9 + 26
    else:
        priority = int(char, 36) - 9
    return priority

helper = 0
sum = 0
with open("input.txt", "r") as file:
    while line := file.readline():
        if helper == 0:
            first = line
            helper += 1
        elif helper == 1:
            second = line
            helper += 1
        else:
            third = line 
            tester = []
            for e in first:
                ep = getPriority(e.strip())
                for p in second:
                    pp = getPriority(p.strip())
                    for q in third:    
                        qp = getPriority(q.strip())
                        if ep == pp and ep == qp:
                            if ep  not in tester:
                                tester.append(ep)
                                sum += ep
            helper = 0

print(sum)
