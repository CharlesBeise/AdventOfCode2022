with open("day5input.txt") as infile:
    rawData = infile.read().split('\n')

data = []

for i in range(10, len(rawData) - 1):
    row = []
    line = rawData[i].split(" ")
    row.append(int(line[1]))
    row.append(int(line[3]))
    row.append(int(line[5]))
    data.append(row)

stack1 = ['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N']
stack2 = ['R', 'S', 'N', 'J', 'H']
stack3 = ['C', 'R', 'N', 'J', 'G', 'Z', 'F', 'Q']
stack4 = ['F', 'V', 'N', 'G', 'R', 'T', 'Q']
stack5 = ['L', 'T', 'Q', 'F']
stack6 = ['Q', 'C', 'W', 'Z', 'B', 'R', 'G', 'N']
stack7 = ['F', 'C', 'L', 'S', 'N', 'H', 'M']
stack8 = ['D', 'N', 'Q', 'M', 'T', 'J']
stack9 = ['P', 'G', 'S']

stacks = [[], stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

for i in range(len(data)):
    for j in range(data[i][0]):
        crate = stacks[data[i][1]].pop()
        stacks[data[i][2]].append(crate)

for s in range(1, len(stacks)):
    print(stacks[s][-1], end="")
