file = open("day15.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

lines = lines[0].split(",")
part1, part2 = 0, 0

for line in lines:
    p = 0
    for char in line:
        p = ((p + ord(char)) * 17) % 256
    part1 += p

print("***** PART 1 *****")
print(part1)
print()

boxes = {}

for i in range(len(lines)):
    p = 0
    j = 0
    while lines[i][j] not in "=-":
        p = ((p + ord(lines[i][j])) * 17) % 256
        j += 1
    if lines[i].endswith("-"):
        if p in boxes:
            boxes[p] = [element for element in boxes[p] if element[:2] != lines[i][:2]]
    else:
        if p in boxes:
            vals = [el[:-2] for el in boxes[p]]
            if lines[i][:-2] in vals:
                index = vals.index(lines[i][:-2])
                boxes[p][index] = lines[i]
            else:
                boxes[p].append(lines[i])
        else:
            boxes[p] = [lines[i]]
for i in range(256):
    if i in boxes:
        for j in range(len(boxes[i])):
            part2 += (i + 1) * (j + 1) * int(boxes[i][j].split("=")[1])


print("***** PART 2 *****")
print(part2)
