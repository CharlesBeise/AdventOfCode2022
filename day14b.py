data = []
with open("day14input.txt") as infile:
    for line in infile.readlines():
        newLine = []
        curLine = line.replace('\n', '').split(' -> ')
        for numLine in curLine:
            temp = numLine.split(',')
            newLine.append([int(temp[0]), int(temp[1])])
        data.append(newLine)

xMin = data[0][0][0]
xMax = 0

yMin = data[0][0][1]
yMax = 0

for i in data:
    for j in i:
        xMin = min(j[0], xMin)
        xMax = max(j[0], xMax)
        yMin = min(j[1], yMin)
        yMax = max(j[1], yMax)

grid = [[' ' for x in range(1001)] for y in range(yMax + 1)]

grid.append([' ' for x in range(len(grid[0]))])
grid.append(['#' for x in range(len(grid[0]))])


def addLine(start, end):
    xDir = 1
    if start[0] > end[0]:
        xDir = -1
    for x in range(start[0], end[0] + xDir, xDir):
        yDir = 1
        if start[1] > end[1]:
            yDir = -1
        for y in range(start[1], end[1] + yDir, yDir):
            grid[y][x] = '#'


for i in range(len(data)):
    for j in range(len(data[i]) - 1):
        addLine(data[i][j], data[i][j + 1])

entrance = [500, 0]


def addSand():
    cur = entrance.copy()
    while True:
        if grid[cur[1] + 1][cur[0]] == ' ':
            cur[1] += 1
        elif grid[cur[1] + 1][cur[0] - 1] == ' ':
            cur[0] -= 1
            cur[1] += 1
        elif grid[cur[1] + 1][cur[0] + 1] == ' ':
            cur[0] += 1
            cur[1] += 1
        else:
            grid[cur[1]][cur[0]] = 'O'
            return True


counter = 0
while addSand():
    counter += 1
    if grid[0][500] == 'O':
        break

print("Answer:", counter)
