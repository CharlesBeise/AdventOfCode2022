"""
SCORING:
1 - Rock
2 - Paper
3 - Scissors

0 - Loss
3 - Draw
6 - Win

MEANINGS:
A - Rock
B - Paper
C - Scissors
X - Loss
Y - Draw
Z - Win
"""



with open("day2input.txt") as infile:
    data = infile.read().replace(" ", '').split('\n')

pointDict = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7
}

score = 0

for i in data:
    score += pointDict[i]

print(score)
