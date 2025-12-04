import re

USE_TEST = 0

if USE_TEST:
    file = open("2018/inputi/day2_test.txt", "r")
else:
    file = open("2018/inputi/day2.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

count2 = 0
count3 = 0

for line in lines:
    match = re.findall(r'(.)', line)
    if any(match.count(c) == 2 for c in match):
        count2 += 1
    if any(match.count(c) == 3 for c in match):
        count3 += 1

print(count2 * count3)

print("***** PART 2 *****")

def similar():
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            diff = 0
            for k in range(len(lines[i])):
                if lines[i][k] != lines[j][k]:
                    diff += 1
            if diff == 1:
                return lines[i], lines[j]
    return None

print(similar())
        