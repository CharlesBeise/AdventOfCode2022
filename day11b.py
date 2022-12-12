import re
import math

monkeys = []
with open("day11input.txt") as infile:
    rawData = infile.readlines()
    # Each Monkey consists of 6 lines of info and a blank line
    for i in range(0, len(rawData), 7):
        curMonkey = {"inspections": 0}

        # Get the starting items
        items = re.findall(r'\d+', rawData[i + 1])
        curMonkey["items"] = [int(item) for item in items]

        # Get the mathematical operation performed
        operation = rawData[i + 2].replace('\n', " ").split(" ")
        if operation[7] == "old":
            operation[6] = "**"
            operation[7] = '2'
        curMonkey["operation"] = [operation[6], int(operation[7])]

        # Get the test condition and resulting actions
        curMonkey["test"] = int(re.findall(r'\d+', rawData[i + 3])[0])
        curMonkey["true"] = int(re.findall(r'\d+', rawData[i + 4])[0])
        curMonkey["false"] = int(re.findall(r'\d+', rawData[i + 5])[0])

        monkeys.append(curMonkey)

values = []
for monkey in monkeys:
    values.append(monkey["test"])

LCM = math.prod(values)


def processMonkey(monkey):
    while len(monkey["items"]) > 0:
        monkey["inspections"] += 1
        # Calculate new stress level
        item = monkey["items"].pop(0)
        op, value = monkey["operation"]
        if op == '+':
            item += value
        elif op == '*':
            item *= value
        elif op == "**":
            item = item ** value

        # Reduce stress on the computer
        item = item % LCM

        # Pass to next Monkey
        if item % monkey["test"] == 0:
            monkeys[monkey["true"]]["items"].append(item)
        else:
            monkeys[monkey["false"]]["items"].append(item)


for i in range(10000):
    for cur in monkeys:
        processMonkey(cur)

best = [0, 0]

for monkey in monkeys:
    if monkey["inspections"] > best[0]:
        best[0] = monkey["inspections"]
        best.sort()

print(best[0] * best[1])
