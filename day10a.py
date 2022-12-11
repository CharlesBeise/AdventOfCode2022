data = []
with open("day10input.txt") as infile:
    for line in infile:
        cur = line.replace('\n', "").split(" ")
        if len(cur) == 1:
            cur.append('0')
        data.append([cur[0], int(cur[1])])


cycle = 1
register = 1
total = 0


def checkCycle(value):
    if cycle in [20, 60, 100, 140, 180, 220]:
        value += (register * cycle)
    return value


for val in data:
    cycle += 1
    total = checkCycle(total)
    if val[0] == "addx":
        cycle += 1
        register += val[1]
        total = checkCycle(total)

print(total)
