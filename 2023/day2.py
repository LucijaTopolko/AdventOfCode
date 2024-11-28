import sys

with open('day2.txt', 'r') as file:
    lines = [line.strip().split(":")[1].split(";") for line in file]

sum = 0
p = 1
part2 = 0
for id, game_info in enumerate(lines, 1):
    p = 1
    s = sys.maxsize
    mr, mb, mg = 0, 0, 0
    for cube_set in game_info:
        red, green, blue = 0, 0, 0
        cube_set = cube_set.split(",")
        for cube in cube_set:
            count, color = cube.split()
            if color == 'red':
                red += int(count)
            elif color == 'green':
                green += int(count)
            else:
                blue += int(count)
        if red > 12 or green > 13 or blue > 14:
            p = 0
        mr = max(mr, red)
        mg = max(mg, green)
        mb = max(mb, blue)

    if p == 1:
        sum += id

    part2 += max(mr, 1) * max(mg, 1) * max(mb, 1)

print("***** PART 1 *****")
print(sum)
print()

print("***** PART 2 *****")
print(part2)
