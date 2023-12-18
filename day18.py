import math
from shapely.geometry.polygon import Polygon

file = open("day18.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

part1, part2 = 0, 0

x, y = 0, 0
corners = [(x, y)]
outline = 1

for line in lines:
    line = line.split(" ")
    length = int(line[1])
    if line[0] == "U":
        x -= length
    elif line[0] == "D":
        x += length
    elif line[0] == "L":
        y -= length
    else:
        y += length
    outline += length
    corners.append((x, y))

shape = Polygon(corners)
part1 = int(shape.area) + math.ceil(outline / 2)

print("***** PART 1 *****")
print(part1)
print()

x, y = 0, 0
corners = [(x, y)]
outline = 1

for line in lines:
    line = line.split(" ")
    length, direction = int(line[2][2:7], 16), int(line[2][7])
    if direction == 3:
        x -= length
    elif direction == 1:
        x += length
    elif direction == 2:
        y -= length
    else:
        y += length
    outline += length
    corners.append((x, y))


shape = Polygon(corners)
part2 = int(shape.area) + math.ceil(outline / 2)

print("***** PART 2 *****")
print(part2)
