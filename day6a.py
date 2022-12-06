with open("day6input.txt") as infile:
    data = infile.readline()

for i in range(3, len(data)):
    chunk = data[i-3:i]
    val = data[i]
    if data[i] not in data[i-3:i]:
        if data[i-1] not in data[i-3:i-1]:
            if data[i-2] != data[i-3]:
                print(i + 1)
                break
