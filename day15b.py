import re

data = []
with open("day15input.txt") as infile:
    for line in infile:
        curRow = []
        nums = re.findall(r'-?\d+', line)
        for num in nums:
            curRow.append(int(num))
        data.append(curRow)

xMin = data[0][0]
xMax = data[0][0]

for v in data:
    xMin = min(xMin, v[0], v[2])
    xMax = max(xMax, v[0], v[2])

maxMan = 0
beacons = set()

for line in data:
    sensor = [line[0], line[1]]
    beacon = (line[2], line[3])
    beacons.add(beacon)
    manDist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    maxMan = max(maxMan, manDist)
    line.append(manDist)


def solve1():
    for y in range(4000001):
        x = 0
        while x < 4000001:
            found = False
            for line in data:
                xDif = abs(line[0] - x)
                yDif = abs(line[1] - y)
                dist = xDif + yDif
                if dist <= line[4]:
                    if x > line[0]:
                        length = line[4] - dist + 1
                    else:
                        length = (2 * line[4]) + 1 - (2 * yDif) - (line[4] - dist)
                    x += length
                    found = True
            if not found:
                print("Answer:", (x * 4000000) + y)
                return


solve1()
