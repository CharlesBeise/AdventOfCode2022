data = []
with open("day9input.txt") as infile:
    lines = infile.read().splitlines()
    row = []
    for line in lines:
        cur = line.split(" ")
        row = [cur[0], int(cur[1])]
        data.append(row)

pos = [0,0]

gridSize = {"Up": 0,
            "Down": 0,
            "Left": 0,
            "Right": 0}

for item in data:
    if item[0] == "U":
        pos[0] += item[1]
        gridSize["Up"] = max(gridSize["Up"], pos[0])
    elif item[0] == "D":
        pos[0] -= item[1]
        gridSize["Down"] = min(gridSize["Down"], pos[0])
    elif item[0] == "L":
        pos[1] -= item[1]
        gridSize["Left"] = min(gridSize["Left"], pos[1])
    else:
        pos[1] += item[1]
        gridSize["Right"] = max(gridSize["Right"], pos[1])

gridHeight = gridSize["Up"] - gridSize["Down"] + 1
gridWidth = gridSize["Right"] - gridSize["Left"] + 1

grid = []
for h in range(gridHeight):
    row = []
    for w in range(gridWidth):
        row.append("_")
    grid.append(row)

rope = []
for i in range(10):
    rope.append([gridSize["Up"], abs(gridSize["Left"])])


grid[rope[0][0]][rope[0][1]] = "S"


def printGrid():
    total = 0
    for row in grid:
        for char in row:
            if char == "#" or char == "T":
                total += 1
    return total


def checkTail(rope, curHead, curTail):
    head = rope[curHead]
    tail = rope[curTail]
    x = head[0] - tail[0]
    y = head[1] - tail[1]

    tempT = [tail[0], tail[1]]
    if curTail == 9:
        grid[tail[0]][tail[1]] = '#'

    if x > 1:
        tail[0] += 1
        if abs(y) != 0:
            if y > 0:
                tail[1] += 1
            else:
                tail[1] -= 1
    elif x < -1:
        tail[0] -= 1
        if abs(y) != 0:
            if y > 0:
                tail[1] += 1
            else:
                tail[1] -= 1
    elif y > 1:
        tail[1] += 1
        if abs(x) != 0:
            tail[0] += x
    elif y < -1:
        tail[1] -= 1
        if abs(x) != 0:
            tail[0] += x

    if curTail == 9:
        grid[tail[0]][tail[1]] = '#'

    if tempT != tail and curTail < len(rope) - 1:
        checkTail(rope, curTail, curTail + 1)


def moveRight(dist):
    for i in range(dist):
        rope[0][1] += 1
        checkTail(rope, 0, 1)


def moveLeft(dist):
    for i in range(dist):
        rope[0][1] -= 1
        checkTail(rope, 0, 1)


def moveUp(dist):
    for i in range(dist):
        rope[0][0] -= 1
        checkTail(rope, 0, 1)


def moveDown(dist):
    for i in range(dist):
        rope[0][0] += 1
        checkTail(rope, 0, 1)


for command in data:
    if command[0] == "R":
        moveRight(command[1])
    elif command[0] == "L":
        moveLeft(command[1])
    elif command[0] == "U":
        moveUp(command[1])
    else:
        moveDown(command[1])

print(printGrid())
