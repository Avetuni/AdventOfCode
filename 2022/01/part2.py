carrying = [0]

elf_num = 0
with open("input.txt", "r") as file:
    while line := file.readline():
        if line == "\n":
            elf_num += 1
            carrying.append(0)
        else:
            carrying[elf_num] += int(line)

st_cals = 0
nd_cals = 0
rd_cals = 0
for e in carrying:
    if e > rd_cals:
        if e > nd_cals:
            if e > st_cals:
                st_cals = e
            else:
                nd_cals = e
        else:
            rd_cals = e
max_cals = st_cals + nd_cals + rd_cals
print(max_cals)