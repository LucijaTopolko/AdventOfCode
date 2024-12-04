file = open("2024/inputi/day4.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

count = 0

for row in range(len(lines)):
    for letter in range(len(lines[row])):
        if lines[row][letter] == 'X':
            if lines[row][letter:(letter+4)] == 'XMAS':
                count += 1
            if lines[row][(letter-3):(letter+1)] == 'SAMX':
                count += 1
            if row + 3 <= len(lines) and lines[row+1][letter] == 'M' and lines[row+2][letter] == 'A' and lines[row+3][letter] == 'S':
                count += 1
            if row - 3 >= 0 and lines[row-1][letter] == 'M' and lines[row-2][letter] == 'A' and lines[row-3][letter] == 'S':
                count += 1

            if row + 3 < len(lines) and letter + 3 < len(lines[row]) and lines[row+1][letter+1] == 'M' and lines[row+2][letter+2] == 'A' and lines[row+3][letter+3] == 'S':
                count += 1
            if row - 3 >= 0 and letter + 3 < len(lines[row]) and lines[row-1][letter+1] == 'M' and lines[row-2][letter+2] == 'A' and lines[row-3][letter+3] == 'S':
                count += 1
            if row + 3 < len(lines) and letter - 3 >= 0 and lines[row+1][letter-1] == 'M' and lines[row+2][letter-2] == 'A' and lines[row+3][letter-3] == 'S':
                count += 1
            if row - 3 >= 0 and letter - 3 >= 0 and lines[row-1][letter-1] == 'M' and lines[row-2][letter-2] == 'A' and lines[row-3][letter-3] == 'S':
                count += 1
            
print(count)

print("***** PART 2 *****")

count = 0

for row in range(1, len(lines) - 1):
    for letter in range(1, len(lines[row]) - 1):
        if lines[row][letter] == 'A':
            if lines[row+1][letter-1] == 'M' and lines[row+1][letter+1] == 'M' and lines[row-1][letter-1] == 'S' and lines[row-1][letter+1] == 'S':
                count += 1
            if lines[row+1][letter-1] == 'S' and lines[row+1][letter+1] == 'S' and lines[row-1][letter-1] == 'M' and lines[row-1][letter+1] == 'M':
                count += 1
            if lines[row+1][letter-1] == 'M' and lines[row-1][letter-1] == 'M' and lines[row-1][letter+1] == 'S' and lines[row+1][letter+1] == 'S':
                count += 1
            if lines[row+1][letter-1] == 'S' and lines[row-1][letter-1] == 'S' and lines[row-1][letter+1] == 'M' and lines[row+1][letter+1] == 'M':
                count += 1
            
print(count)