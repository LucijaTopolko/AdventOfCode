file = open("day13.txt", "r")
lines = file.read()
lines = lines.split("\n\n")

for i in range(len(lines)):
    lines[i] = lines[i].split("\n")

part1, part2 = 0, 0

for l in lines:
    # stupci
    for j in range(len(l[0]) - 1):
        nsame = 0
        for i in range(len(l)):
            if l[i][j] != l[i][j + 1]:
                nsame = 1
        if not nsame:
            check = min(j, len(l[0]) - j - 2)
            different = 0
            for c in range(1, check + 1):
                for i in range(len(l)):
                    if l[i][j - c] != l[i][j + 1 + c]:
                        different = 1
            if not different:
                part1 += j + 1

    # retci
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            check = min(i, len(l) - i - 2)
            different = 0
            for r in range(1, check + 1):
                if l[i - r] != l[i + 1 + r]:
                    different = 1
            if not different:
                part1 += 100 * (i + 1)

print("***** PART 1 *****")
print(part1)
print()

for i in range(len(lines)):
    l = lines[i]
    for j in range(len(l[0]) - 1):
        diff = 0
        for k in range(len(l)):
            if l[k][j] != l[k][j + 1]:
                diff += 1
        if diff == 1:
            check = min(j, len(l[0]) - j - 2)
            different = 0
            for c in range(1, check + 1):
                for t in range(len(l)):
                    if l[t][j - c] != l[t][j + 1 + c]:
                        different = 1
            if not different:
                part2 += j + 1
        elif diff == 0:
            check = min(j, len(l[0]) - j - 2)
            different = 0
            for c in range(1, check + 1):
                for t in range(len(l)):
                    if l[t][j - c] != l[t][j + 1 + c]:
                        different += 1
            if different == 1:
                part2 += j + 1

    for k in range(len(l) - 1):
        diff = 0
        for j in range(len(l[0])):
            if l[k][j] != l[k + 1][j]:
                diff += 1
        if diff == 1:
            check = min(k, len(l) - k - 2)
            different = 0
            for r in range(1, check + 1):
                if l[k - r] != l[k + 1 + r]:
                    different = 1
            if not different:
                part2 += 100 * (k + 1)
                break
        elif diff == 0:
            check = min(k, len(l) - k - 2)
            different = 0
            for r in range(1, check + 1):
                if l[k - r] != l[k + 1 + r]:
                    different += 1
            if different == 1:
                part2 += 100 * (k + 1)


print("***** PART 2 *****")
print(part2)
