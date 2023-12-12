import numpy as np

with open("day4.txt", "r") as file:
    lines = [line.strip() for line in file]

print(lines)
part1, part2 = 0, 0
for i in range(len(lines)):
    p = 0
    lines[i] = lines[i][8:].split(" | ")
    a = lines[i][0].split()
    b = lines[i][1].split()
    for num in a:
        if num in b:
            if p == 0:
                p = 1
            else:
                p *= 2
    part1 += p


print("***** PART 1 *****")
print(part1)
print()

r = np.ones(len(lines))
r[0] = 1
for i in range(len(lines)):
    p = 0
    a = lines[i][0].split()
    b = lines[i][1].split()
    for num in a:
        if num in b:
            p += 1
    for k in range(int(p)):
        try:
            r[i + k + 1] += r[i]
        except:
            pass

part2 = sum(r)
print("***** PART 2 *****")
print(part2)
