with open("day6input.txt") as infile:
    data = infile.readline()


def checkMessage(block, value):
    if len(block) == 1:
        return True
    elif value in block:
        return False
    else:
        return checkMessage(block[:-1], block[-1])


for i in range(13, len(data)):
    chunk = data[i-13:i]
    val = data[i]
    if checkMessage(chunk, val):
        print(i + 1)
        break
