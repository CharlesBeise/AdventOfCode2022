import re

data = []
with open("day4input.txt") as infile:
    for line in infile:
        data.append(re.split(r'[-,\n]', line))

total = 0

for item in data:
    one, two, three, four, blank = item
    if (int(one) >= int(three)) and (int(two) <= int(four)):
        total += 1
    elif (int(three) >= int(one)) and (int(four) <= int(two)):
        total += 1

print(total)
