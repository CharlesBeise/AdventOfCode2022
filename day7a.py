import re

data = []
with open("day7input.txt") as infile:
    for line in infile:
        data.append(re.split(" ", line.replace('\n', "")))

dirDict = {"/": {"size": 0, "dicts": []}}
dirList = ["/"]

curDir = "/"
curSize = 0

data = data[1:]
data.append(["$", "cd", ".."])

for i in range(len(data)):
    cur = data[i]
    if cur[0] == "$":
        if cur[1] == "cd":
            # Backing out of a directory
            if cur[2] == "..":
                dirDict[curDir]["size"] = dirDict[curDir]["size"] + curSize
                while curDir[-1] != "/":
                    curDir = curDir[:-1]
                curDir = curDir[:-1]
            # Stepping into a directory
            else:
                dirDict[curDir]["size"] = dirDict[curDir]["size"] + curSize
                curDir = curDir + "/" + cur[2]
                dirDict[curDir] = {"size": 0, "dicts": []}
                dirList.append(curDir)
            curSize = 0
    elif cur[0] == "dir":
        dirDict[curDir]["dicts"].append(curDir + "/" + cur[1])
    else:
        curSize += int(cur[0])

for j in range(len(dirList) - 1, -1, -1):
    curDir = dirDict[dirList[j]]
    for item in curDir["dicts"]:
        curDir["size"] = curDir["size"] + dirDict[item]["size"]


total = 0
for keys, vals in dirDict.items():
    if dirDict[keys]["size"] <= 100000:
        total += vals["size"]

print(total)
