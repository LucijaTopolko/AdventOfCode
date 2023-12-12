import numpy as np

file = open("day10.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

start_position = [
    (i, j) for i, row in enumerate(lines) for j, col in enumerate(row) if col == "S"
][0]

ax, ay = start_position[0], start_position[1]

part1, part2 = 1, 0

rows, cols = len(lines), len(lines[0])
isInPath = np.zeros((rows, cols))
isInPath[ax][ay] = 1
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # desno, dolje, lijevo, gore
correct = ["-7J", "|LJ", "-FL", "|7F"]
S_neighbours = []
for i in range(len(dirs)):
    p = dirs[i]
    bx = ax + p[0]
    by = ay + p[1]  # na novoj poziciji
    if 0 <= bx < rows and 0 <= by < cols and lines[bx][by] in correct[i]:
        S_neighbours.append(i)

valid = 3 in S_neighbours

curr = S_neighbours[0]
cx, cy = ax + dirs[curr][0], ay + dirs[curr][1]

transitions = {
    (0, "-"): 0,
    (0, "7"): 1,
    (0, "J"): 3,
    (1, "|"): 1,
    (1, "L"): 0,
    (1, "J"): 2,
    (2, "-"): 2,
    (2, "F"): 1,
    (2, "L"): 3,
    (3, "|"): 3,
    (3, "7"): 2,
    (3, "F"): 0,
}

while (cx, cy) != (ax, ay):
    part1 += 1
    isInPath[cx][cy] = 1
    curr = transitions.get((curr, lines[cx][cy]), curr)  # kamo ide dalje
    cx, cy = cx + dirs[curr][0], cy + dirs[curr][1]

print("***** PART 1 *****")
print(part1 // 2)
print()

for i in range(0, rows - 1):
    p = 0
    for j in range(0, cols - 1):
        if isInPath[i][j]:
            if lines[i][j] in "|LJ" or (lines[i][j] == "S" and valid):
                p += 1
        else:
            if p % 2 == 1:
                # print(i, j)
                part2 += 1

print("***** PART 2 *****")
print(part2)
