import re

data = []
with open("day4input.txt") as infile:
    for line in infile:
        data.append(re.split(r'[-,\n]', line))

total = 0

for item in data:
    one, two, three, four, blank = item
    elf1 = [int(one), int(two)]
    elf2 = [int(three), int(four)]
    if elf2[0] <= elf1[0] <= elf2[1]:
        total += 1
    elif elf2[0] <= elf1[1] <= elf2[1]:
        total += 1
    elif elf1[0] <= elf2[0] <= elf1[1]:
        total += 1
    elif elf1[0] <= elf2[1] <= elf1[1]:
        total += 1

print(total)
