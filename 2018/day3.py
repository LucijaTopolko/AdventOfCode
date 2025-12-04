USE_TEST = 0

if USE_TEST:
    file = open("2018/inputi/day3_test.txt", "r")
else:
    file = open("2018/inputi/day3.txt", "r")

lines = file.readlines()
lines1 = []
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]
    lines1.append(lines[i].split(" @ ")[1])

print("***** PART 1 *****")

grid = [[0 for i in range(1000)] for j in range(1000)]
overlaps = set()

for line in lines1:
    corner, dimensions = line.split(": ")
    x, y = corner.split(",")
    w, h = dimensions.split("x")
    for j in range(int(h)):
        for i in range(int(w)):
            if grid[int(x)+i][int(y)+j] != 0:
                overlaps.add((int(x)+i, int(y)+j))
            grid[int(x)+i][int(y)+j] += 1
        
print(len(overlaps))

print("***** PART 2 *****")

pure = 0

for line in lines:
    id, other = line.split(" @ ")
    id = id[1:]
    corner, dimensions = other.split(": ")
    x, y = corner.split(",")
    w, h = dimensions.split("x")
    good = True
    for j in range(int(h)):
        for i in range(int(w)):
            if grid[int(x)+i][int(y)+j] != 1:
                good = False
    if good:
        pure = id

print(pure)
