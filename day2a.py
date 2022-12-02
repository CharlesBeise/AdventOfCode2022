"""
SCORING:
1 - Rock
2 - Paper
3 - Scissors

0 - Loss
3 - Draw
6 - Win

MEANINGS:
A/X - Rock
B/Y - Paper
C/Z - Scissors
"""



with open("day2input.txt") as infile:
    data = infile.read().replace(" ", '').split('\n')

pointDict = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6
}

score = 0

for i in data:
    score += pointDict[i]

print(score)
