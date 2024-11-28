file = open("day14.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]


def calculate(z):
    part = 0
    for i in range(len(z)):
        for j in range(len(z[0])):
            if z[i][j] == "O":
                part += len(z) - i
    return part


def movenorth(lines):
    z = [[0] * len(lines[0]) for _ in range(len(lines))]
    for j in range(len(lines[0])):
        place = 0
        for i in range(len(lines)):
            if lines[i][j] == "#":
                z[i][j] = "#"
                place = i + 1
            elif lines[i][j] == "O":
                z[place][j] = "O"
                place += 1
    return z


print("***** PART 1 *****")
print(calculate(movenorth(lines)))
print()


def movewest(lines):
    z = [[0] * len(lines[0]) for _ in range(len(lines))]
    for i in range(len(lines)):
        place = 0
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                z[i][j] = "#"
                place = j + 1
            elif lines[i][j] == "O":
                z[i][place] = "O"
                place += 1
    return z


def movesouth(lines):
    z = [[0] * len(lines[0]) for _ in range(len(lines))]
    for j in range(len(lines[0])):
        place = len(lines) - 1
        for i in reversed(range(len(lines))):
            if lines[i][j] == "#":
                z[i][j] = "#"
                place = i - 1
            elif lines[i][j] == "O":
                z[place][j] = "O"
                place -= 1
    return z


def moveeast(lines):
    z = [[0] * len(lines[0]) for _ in range(len(lines))]
    for i in range(len(lines)):
        place = len(lines[0]) - 1
        for j in reversed(range(len(lines[0]))):
            if lines[i][j] == "#":
                z[i][j] = "#"
                place = j - 1
            elif lines[i][j] == "O":
                z[i][place] = "O"
                place -= 1
    return z


old = {}
c = 1000000000
for x in range(c):
    lines = moveeast(movesouth(movewest(movenorth(lines))))
    tuple_lines = tuple(tuple(a) for a in lines)
    if tuple_lines in old:
        diff = x - old[tuple_lines]
        c = (c - x) % diff - 1
        break
    old[tuple_lines] = x
for x in range(c):
    lines = moveeast(movesouth(movewest(movenorth(lines))))

print("***** PART 2 *****")
print(calculate(lines))
