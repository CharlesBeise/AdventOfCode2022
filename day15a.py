import re

data = []
targetNum = 2000000
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

total = 0

i = -maxMan
while i < xMax - xMin + maxMan:
    for line in data:
        dist = abs(line[0] - i) + abs(line[1] - targetNum)
        if dist <= line[4]:
            length = (2 * line[4]) + 1 - (2 * (abs(line[1] - targetNum))) - (line[4] - dist)
            total += length
            i += length - 1
            break
    i += 1

for b in beacons:
    if b[1] == targetNum:
        total -= 1

print(total)
