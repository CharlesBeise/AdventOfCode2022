data = []

with open("day1ainput.txt") as infile:
    for line in infile:
        data.append(line.strip('\n'))

maximum = 0
current = 0

for i in data:
    if i == "":
        if current > maximum:
            maximum = current
        current = 0
    else:
        current += int(i)

print(maximum)
