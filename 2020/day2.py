USE_TEST = 0

if USE_TEST:
    file = open("2020/inputi/day2_test.txt", "r")
else:
    file = open("2020/inputi/day2.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

result = 0

for line in lines:
    rule, password = line.split(": ")
    letter = rule.split(" ")[1]
    min, max = rule.split(" ")[0].split("-")
    min = int(min)
    max = int(max)
    count = password.count(letter)
    if count >= min and count <= max:
        result += 1
print(result)

print("***** PART 2 *****")

result = 0

for line in lines:
    rule, password = line.split(": ")
    letter = rule.split(" ")[1]
    pos1, pos2 = rule.split(" ")[0].split("-")
    pos1 = int(pos1) -1
    pos2 = int(pos2) -1
    c = 0
    if password[pos1] == letter:
        c += 1
    if password[pos2] == letter:
        c += 1
    if c == 1:
        result += 1
print(result)