USE_TEST = 0

if USE_TEST:
    file = open("2025/inputi/day4_test.txt", "r")
else:
    file = open("2025/inputi/day4.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

def check(lines, l, i):
    c = 0
    if i+1 < len(lines[l]) and lines[l][i+1] == '@':
        c += 1
    if i-1 >= 0 and lines[l][i-1] == '@':
        c += 1
    if l-1 >= 0 and i+1 < len(lines[l-1]) and lines[l-1][i+1] == '@':
        c += 1
    if l-1 >= 0 and i-1 >= 0 and lines[l-1][i-1] == '@':
        c += 1
    if l-1 >= 0 and lines[l-1][i] == '@':
        c += 1
    if l+1 < len(lines) and i+1 < len(lines[l+1]) and lines[l+1][i+1] == '@':
        c += 1
    if l+1 < len(lines) and i-1 >= 0 and lines[l+1][i-1] == '@':
        c += 1
    if l+1 < len(lines) and lines[l+1][i] == '@':
        c += 1
    return c

print("***** PART 1 *****")

count = 0

lines = [list(line) for line in lines]
for l in range(len(lines)):
    for i in range(len(lines[l])):
        if lines[l][i] == '@':
            c = check(lines, l, i)
            if c < 4:
                count += 1
            
print(count)

print("***** PART 2 *****")

count = 0

lines = [list(line) for line in lines]

new_lines = lines.copy()
changes = True
while changes:
    changes = False
    for l in range(len(lines)):
        for i in range(len(lines[l])):
            if lines[l][i] == '@':
                c = check(lines, l, i)
                if c < 4:
                    count += 1
                    new_lines[l][i] = '.'
                    changes = True
        lines = new_lines.copy()
            
print(count)
