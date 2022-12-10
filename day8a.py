grid = []
with open("day8input.txt") as infile:
    for line in infile:
        row = []
        for char in line.replace('\n', ""):
            row.append(int(char))
        grid.append(row)


def checkUp(height, width, curTree):
    for up in range(height - 1, -1, -1):
        if grid[up][width] >= curTree:
            return False
    return True


def checkDown(height, width, curTree):
    for down in range(height + 1, len(grid)):
        if grid[down][width] >= curTree:
            return False
    return True


def checkLeft(height, width, curTree):
    for left in range(width - 1, -1, -1):
        if grid[height][left] >= curTree:
            return False
    return True


def checkRight(height, width, curTree):
    for right in range(width + 1, len(grid[height])):
        if grid[height][right] >= curTree:
            return False
    return True


def checkVisible(height, width):
    curTree = grid[height][width]
    if checkUp(height, width, curTree):
        return True
    elif checkDown(height, width, curTree):
        return True
    elif checkRight(height, width, curTree):
        return True
    else:
        return checkLeft(height, width, curTree)



visible = 0

for h in range(len(grid)):
    for w in range(len(grid[h])):
        if checkVisible(h, w):
            visible += 1

print(visible)
