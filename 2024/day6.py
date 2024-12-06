import time

file = open("2024/inputi/day6.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = list(lines[i].split("\n")[0])

print("***** PART 1 *****")

start = []
visited = set()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            start = [i, j] 

i, j = start[0], start[1]

dir = 'N'

next_move = {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}

movements = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1 ,0)}

while 0 <= i <= len(lines[0]) and 0 <= j <= len(lines):
    visited.add(tuple([i,j]))
    move = movements[dir]
    if len(lines[0]) > i + move[0] >= 0 and 0 <= j + move[1] < len(lines):
        a = i + move[0]
        b = j + move[1]
        if lines[a][b] == '.' or lines[a][b] == '^':
            i, j = a, b
        else: 
            dir = next_move[dir]
    else: 
        break

print(len(visited))

print("***** PART 2 *****")

count = 0

for row, col in visited:
    if lines[row][col] == '#':
        continue

    i, j = start[0], start[1]
    visited = set()
    dir = 'N'
    while 0 <= i <= len(lines[0]) and 0 <= j <= len(lines):
        move = movements[dir]
        if len(lines[0]) > i + move[0] >= 0 and 0 <= j + move[1] < len(lines):
            a = i + move[0]
            b = j + move[1]
            if (lines[a][b] == '.' or lines[a][b] == '^') and (a != row or b != col):
                i, j = a, b
            else: 
                dir = next_move[dir]
        else: 
            break
        if tuple([i,j, dir]) not in visited:
            visited.add(tuple([i,j, dir]))
        else:
            count += 1
            break

print(count)