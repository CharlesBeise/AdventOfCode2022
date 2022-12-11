data = []
with open("day10input.txt") as infile:
    for line in infile:
        cur = line.replace('\n', "").split(" ")
        if len(cur) == 1:
            cur.append('0')
        data.append([cur[0], int(cur[1])])


cycle = 0
register = 1
screen = ""


def checkCycle(result):
    if register - 1 <= cycle <= register + 1:
        result += '#'
    else:
        result += '.'
    return result


for val in data:
    screen = checkCycle(screen)
    cycle = (cycle + 1) % 40
    if val[0] == "addx":
        screen = checkCycle(screen)
        cycle = (cycle + 1) % 40
        register += val[1]

counter = 0
for char in screen:
    if counter % 40 == 0:
        print()
    print(char, end="")
    counter += 1
