with open("day3input.txt") as infile:
    data = infile.read().split('\n')

total = 0

for i in range(len(data) - 1):
    cur = data[i]
    mid = len(cur)//2
    first = cur[:mid]
    second = cur[mid:]

    for letter in first:
        if letter in second:
            value = ord(letter) - 96
            if value < 0:
                value += 58
            total += value
            break

print(total)
