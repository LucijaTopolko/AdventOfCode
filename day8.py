import math

file = open("day8.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

part1, part2 = 0, []

my_dict = {}
directions = lines[0]
lines = lines[2:]
for i in lines:
    parts = i.split("=")
    variable = parts[0].strip()
    dependencies = tuple(part.strip() for part in parts[1][2:-1].split(","))
    my_dict[variable] = dependencies

condition = lambda last, flag: (flag == 1 and last != "ZZZ") or (
    flag == 2 and not last.endswith("Z")
)

last = "AAA"


def solve(last, part):
    p = 0
    while condition(last, part):
        for dir in directions:
            lastVar = my_dict.get(last, None)
            if dir == "L":
                last = lastVar[0]
            else:
                last = lastVar[1]
            p += 1
            if not condition(last, part):
                break
    return p


print("***** PART 1 *****")
print(solve("AAA", 1))
print()

last = [key for key in my_dict.keys() if key.endswith("A")]

for el in last:
    part2.append(solve(el, 2))

print("***** PART 2 *****")
print(math.lcm(*part2))
