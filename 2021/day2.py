USE_TEST = 0

if USE_TEST:
    file = open("2021/inputi/day2_test.txt", "r")
else:
    file = open("2021/inputi/day2.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

pos = [0, 0]
for line in lines:
    direction, amount = line.split(" ")
    amount = int(amount)
    if direction == "forward":
        pos[0] += amount
    elif direction == "down":
        pos[1] += amount
    elif direction == "up":
        pos[1] -= amount
print(pos[0] * pos[1])

print("***** PART 2 *****")

pos = [0, 0, 0]
for line in lines:
    direction, amount = line.split(" ")
    amount = int(amount)
    if direction == "forward":
        pos[0] += amount
        pos[1] += pos[2] * amount
    elif direction == "down":
        pos[2] += amount
    elif direction == "up":
        pos[2] -= amount
print(pos[0] * pos[1])
