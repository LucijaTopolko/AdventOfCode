from heapq import *

file = open("day17.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

part1, part2 = 0, 0

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # desno, dolje, lijevo, gore


def dijkstra(minsteps, maxsteps):
    heap = [(0, 0, 0, -1)]  # cijena, x, y, smjer
    visited = set()
    costs = {}
    while heap:
        cost, x, y, direction = heappop(heap)
        if (x, y, direction) in visited:
            continue
        if x == len(lines) - 1 and y == len(lines[0]) - 1:
            return cost
        visited.add((x, y, direction))
        for d in range(len(directions)):
            extracost = 0
            if d == direction or (d + 2) % 4 == direction:
                continue  # preskačemo ove u istom smjeru i ove koji se vraćaju istim putem
            for distance in range(1, maxsteps + 1):
                xb, yb = (
                    x + directions[d][0] * distance,
                    y + directions[d][1] * distance,
                )
                if 0 <= xb < len(lines) and 0 <= yb < len(lines[0]):
                    extracost += int(lines[xb][yb])
                    if distance >= minsteps:
                        newcost = cost + extracost
                        oldcost = costs.get((xb, yb, d))
                        if not oldcost or oldcost > newcost:
                            costs[(xb, yb, d)] = newcost
                            heappush(heap, (newcost, xb, yb, d))


print("***** PART 1 *****")
print(dijkstra(1, 3))
print()

print("***** PART 2 *****")
print(dijkstra(4, 10))
