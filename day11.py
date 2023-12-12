file = open("day11.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

d_rows = [i for i, row in enumerate(lines) if all(cell == "." for cell in row)]
d_cols = [j for j in range(len(lines[0])) if all(row[j] == "." for row in lines)]


galaxies = [
    (i, j) for i, row in enumerate(lines) for j, col in enumerate(row) if col == "#"
]


def solve(a, b):
    sum1, sum2 = 0, 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            ax, ay = galaxies[i]
            bx, by = galaxies[j]
            if by < ay:
                ay, by = by, ay
            t1, t2 = bx - ax + by - ay, bx - ax + by - ay
            for l in range(ax, bx):
                if l in d_rows:
                    t1 += a
                    t2 += b
            for k in range(ay, by):
                if k in d_cols:
                    t1 += a
                    t2 += b
            sum1 += t1
            sum2 += t2
    return sum1, sum2


part1, part2 = solve(1, 1000000 - 1)

print("***** PART 1 *****")
print(part1)
print()

print("***** PART 2 *****")
print(part2)
