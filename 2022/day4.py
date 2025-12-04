USE_TEST = 0

if USE_TEST:
    file = open("2022/inputi/day4_test.txt", "r")
else:
    file = open("2022/inputi/day4.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")
for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    for j in range(2):
        lines[i][j] = lines[i][j].split("-")
        lines[i][j] = list(map(int, lines[i][j]))

res = 0
for i in range(len(lines)):
    if lines[i][0][0] <= lines[i][1][0] and lines[i][0][1] >= lines[i][1][1]:
        res += 1
    elif lines[i][1][0] <= lines[i][0][0] and lines[i][1][1] >= lines[i][0][1]:
        res += 1

print(res)

print("***** PART 2 *****")

res = 0

for i in range(len(lines)):
    if lines[i][0][0] >= lines[i][1][0] and lines[i][0][0] <= lines[i][1][1]:
        res += 1
    elif lines[i][0][1] >= lines[i][1][0] and lines[i][0][1] <= lines[i][1][1]:
        res += 1
    elif lines[i][1][0] >= lines[i][0][0] and lines[i][1][0] <= lines[i][0][1]:
        res += 1
    elif lines[i][1][1] >= lines[i][0][0] and lines[i][1][1] <= lines[i][0][1]:
        res += 1

print(res)
