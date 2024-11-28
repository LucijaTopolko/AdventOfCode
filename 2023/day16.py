import sys

sys.setrecursionlimit(5000)

file = open("day16.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]


def count(startx, starty, direction):
    energized = set()

    def go(x, y, direct):
        if (x, y, direct) in energized:
            return
        energized.add((x, y, direct))
        el = lines[x][y]
        if el == ".":
            if direct == "R" and y < (len(lines) - 1):
                go(x, y + 1, "R")
            elif direct == "L" and y > 0:
                go(x, y - 1, "L")
            elif direct == "U" and x > 0:
                go(x - 1, y, "U")
            elif direct == "D" and x < (len(lines[0]) - 1):
                go(x + 1, y, "D")
        elif el == "/":
            if direct == "R" and x > 0:
                go(x - 1, y, "U")
            elif direct == "L" and x < (len(lines[0]) - 1):
                go(x + 1, y, "D")
            elif direct == "U" and y < (len(lines) - 1):
                go(x, y + 1, "R")
            elif direct == "D" and y > 0:
                go(x, y - 1, "L")
        elif el == "\\":
            if direct == "R" and x < (len(lines[0]) - 1):
                go(x + 1, y, "D")
            elif direct == "L" and x > 0:
                go(x - 1, y, "U")
            elif direct == "U" and y > 0:
                go(x, y - 1, "L")
            elif direct == "D" and y < (len(lines) - 1):
                go(x, y + 1, "R")
        elif el == "-":
            if direct == "R" and y < (len(lines) - 1):
                go(x, y + 1, "R")
            elif direct == "L" and y > 0:
                go(x, y - 1, "L")
            elif direct == "U":
                if y > 0:
                    go(x, y - 1, "L")
                if y < (len(lines) - 1):
                    go(x, y + 1, "R")
            elif direct == "D":
                if y > 0:
                    go(x, y - 1, "L")
                if y < (len(lines) - 1):
                    go(x, y + 1, "R")
        elif el == "|":
            if direct == "R":
                if x > 0:
                    go(x - 1, y, "U")
                if x < (len(lines[0]) - 1):
                    go(x + 1, y, "D")
            elif direct == "L":
                if x > 0:
                    go(x - 1, y, "U")
                if x < (len(lines[0]) - 1):
                    go(x + 1, y, "D")
            elif direct == "U" and x > 0:
                go(x - 1, y, "U")
            elif direct == "D" and x < (len(lines[0]) - 1):
                go(x + 1, y, "D")

    go(startx, starty, direction)

    final = set()
    for element in energized:
        final.add((element[0], element[1]))
    return len(final)


part1 = count(0, 0, "R")

print("***** PART 1 *****")
print(part1)
print()

part2 = 0

for i in range(len(lines)):
    part2 = max(part2, count(i, 0, "R"), count(i, len(lines[0]) - 1, "L"))

for j in range(len(lines[0])):
    part2 = max(part2, count(0, j, "D"), count(len(lines) - 1, j, "U"))

print("***** PART 2 *****")
print(part2)
