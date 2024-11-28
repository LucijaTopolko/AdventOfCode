file = open("day9.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

part1, part2, p2 = 0, 0, 0
for i in range(len(lines)):
    p2 = 0
    line = [lines[i].split(" ")]
    while not all(value == 0 for value in line[-1]):
        a = []
        for j in range(len(line[-1]) - 1):
            a.append(-int(line[-1][j]) + int(line[-1][j + 1]))
        line.append(a)
    for k in range(len(line)):
        part1 += int(line[k][-1])
    for k in range(len(line) - 1, -1, -1):
        p2 = int(line[k][0]) - p2
    part2 += p2

print("***** PART 1 *****")
print(part1)
print()
print("***** PART 2 *****")
print(part2)
