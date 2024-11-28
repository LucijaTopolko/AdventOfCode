with open('day3.txt', 'r') as file:
    lines = [line.strip() for line in file]

part1, part2 = 0, 0

for i in range(len(lines)):
    j = 0
    while j < len(lines[i]):
        a = 0
        if lines[i][j].isdigit():
            b = ""
            while j < len(lines[i]) and lines[i][j].isdigit():
                b += lines[i][j]
                j += 1
            j -= len(b)
            for k in range(0, len(b)):
                if j > 0 and (not lines[i][j - 1].isdigit()) and ord(lines[i][j - 1]) != 46:  # lijevo
                    a = 1
                if j < (len(lines[i]) - 1):
                    if (not lines[i][j + 1].isdigit()) and ord(lines[i][j + 1]) != 46:  # desno
                        a = 1
                if i > 0:
                    if (not lines[i - 1][j].isdigit()) and ord(lines[i - 1][j]) != 46:  # gore
                        a = 1
                    if j > 0:
                        if (not lines[i - 1][j - 1].isdigit()) and ord(lines[i - 1][j - 1]) != 46:  # gore lijevo
                            a = 1
                    if j < (len(lines[i]) - 2):
                        if (not lines[i - 1][j + 1].isdigit()) and ord(lines[i - 1][j + 1]) != 46:  # gore deno
                            a = 1
                if i < ((len(lines)) - 1):
                    if (not lines[i + 1][j].isdigit()) and ord(lines[i + 1][j]) != 46:
                        a = 1
                    if j > 0:
                        if (not lines[i + 1][j - 1].isdigit()) and ord(lines[i + 1][j - 1]) != 46:
                            a = 1
                    if j < (len(lines[i]) - 2):
                        if (not lines[i + 1][j + 1].isdigit()) and ord(lines[i + 1][j + 1]) != 46:
                            a = 1
                j += 1
            if a == 1:
                part1 += int(b)
        else:
            j += 1

print("***** PART 1 *****")
print(part1)
print()

t = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        a = 0
        m = 1
        if lines[i][j] == "*":
            s = set()
            if j > 0 and lines[i][j - 1].isdigit():  # left
                t = j
                while j > 0 and lines[i][j - 1].isdigit():
                    j -= 1
                if not lines[i][j].isdigit():
                    j += 1
                s.add((i, j))
                j = t
            if j < (len(lines[i]) - 1) and lines[i][j + 1].isdigit():  # right
                t = j
                while j > 0 and lines[i][j + 1].isdigit():
                    j -= 1
                if not lines[i][j + 1].isdigit():
                    j += 1
                s.add((i, j + 1))
                j = t
            if i > 0:
                if lines[i - 1][j].isdigit():  # up
                    t = j
                    while j > 0 and lines[i - 1][j].isdigit():
                        j -= 1
                    if not lines[i - 1][j].isdigit():
                        j += 1
                    s.add((i - 1, j))
                    j = t
                if j > 0 and lines[i - 1][j - 1].isdigit():  # up left
                    t = j
                    while j > 0 and lines[i - 1][j - 1].isdigit():
                        j -= 1
                    if not lines[i - 1][j].isdigit():
                        j += 1
                    s.add((i - 1, j))
                    j = t
                if j < (len(lines[i]) - 2) and lines[i - 1][j + 1].isdigit():  # up right
                    t = j
                    while j > 0 and lines[i - 1][j + 1].isdigit():
                        j -= 1
                    if not lines[i - 1][j + 1].isdigit():
                        j += 1
                    s.add((i - 1, j + 1))
                    j = t
            if i < (len(lines) - 1):
                if lines[i + 1][j].isdigit():  # down
                    t = j
                    while j > 0 and lines[i + 1][j].isdigit():
                        j -= 1
                    if not lines[i + 1][j].isdigit():
                        j += 1
                    s.add((i + 1, j))
                    j = t
                if j > 0 and lines[i + 1][j - 1].isdigit():  # down left
                    t = j
                    while j > 0 and lines[i + 1][j - 1].isdigit():
                        j -= 1
                    if not lines[i + 1][j].isdigit():
                        j += 1
                    s.add((i + 1, j))
                    j = t
                if j < (len(lines[i]) - 2) and lines[i + 1][j + 1].isdigit():  # down right
                    t = j
                    while j > 0 and lines[i + 1][j + 1].isdigit():
                        j -= 1
                    if not lines[i + 1][j + 1].isdigit():
                        j += 1
                    s.add((i + 1, j + 1))
                    j = t
            if len(s) == 2:
                m = 1
                for k, l in s:
                    b = ""
                    while l < len(lines[k]) and lines[k][l].isdigit():
                        b += lines[k][l]
                        l += 1
                    m *= int(b)
                part2 += m

print("***** PART 2 *****")
print(part2)
