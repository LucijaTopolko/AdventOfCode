import re

USE_TEST = 0

if USE_TEST:
    file = open("2025/inputi/day2_test.txt", "r")
else:
    file = open("2025/inputi/day2.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

line = lines[0].split(",")
for i in range(len(line)):
    line[i] = line[i].split("-")
    line[i] = list(map(int, line[i]))

print("***** PART 1 *****")

count = 0
for i in line:
    for j in range(i[0], i[1] + 1):
        p = len(str(j))
        j = str(j)
        if j[:p//2] == j[p//2:]:
            count += int(j)

print(count)

print("***** PART 2 *****")

count = 0

for i in line:
    for j in range(i[0], i[1] + 1):
        if re.fullmatch(r'(.+)\1+', str(j)) != None:
            count += int(j)

print(count)