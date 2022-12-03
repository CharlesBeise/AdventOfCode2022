with open("day3input.txt") as infile:
    data = infile.read().split('\n')

total = 0

for i in range(0, len(data) - 2, 3):
    first = data[i]
    second = data[i + 1]
    third = data[i + 2]

    for letter in first:
        if letter in second:
            if letter in third:
                value = ord(letter) - 96
                if value < 0:
                    value += 58
                total += value
                break

print(total)
