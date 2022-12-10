grid = []
with open("day8input.txt") as infile:
    for line in infile:
        row = []
        for char in line.replace('\n', ""):
            row.append(int(char))
        grid.append(row)


def checkUp(height, width, curTree):
    score = 0
    for up in range(height - 1, -1, -1):
        score += 1
        if grid[up][width] >= curTree:
            break
    return score


def checkDown(height, width, curTree):
    score = 0
    for down in range(height + 1, len(grid)):
        score += 1
        if grid[down][width] >= curTree:
            break
    return score


def checkLeft(height, width, curTree):
    score = 0
    for left in range(width - 1, -1, -1):
        score += 1
        if grid[height][left] >= curTree:
            break
    return score


def checkRight(height, width, curTree):
    score = 0
    for right in range(width + 1, len(grid[height])):
        score += 1
        if grid[height][right] >= curTree:
            break
    return score


def checkScore(height, width):
    curTree = grid[height][width]
    score = 1
    score *= checkUp(height, width, curTree)
    score *= checkDown(height, width, curTree)
    score *= checkRight(height, width, curTree)
    score *= checkLeft(height, width, curTree)
    return score



scenicScore = 0

for h in range(len(grid)):
    for w in range(len(grid[h])):
        scenicScore = max(scenicScore, checkScore(h, w))

print(scenicScore)
