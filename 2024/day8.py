file = open("2024/inputi/day8.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = list(lines[i].split("\n")[0])

print("***** PART 1 *****") 

antinodes1 = set()
antinodes2 = set()

def antinode(x1, y1, x2, y2):
    x = x2 + (x2 - x1)
    y = y2 + (y2 - y1)
    antinodes2.add((x2, y2))
    if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        antinodes1.add((x,y))
        while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            antinodes2.add((x, y))
            x += (x2 - x1)
            y += (y2 - y1)

count = 0
signals = set(element for sublist in lines for element in sublist if element != '.')
signalpositions = {}

for signal in signals:
    positions = set()
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            if lines[i][j] == signal:
                positions.add(tuple([i,j]))
    positions = list(positions)
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            antinode(x1, y1, x2, y2)
            antinode(x2, y2, x1, y1)

print(len(antinodes1))

print("***** PART 2 *****")

print(len(antinodes2))