USE_TEST = 0

if USE_TEST:
    file = open("2025/inputi/day1_test.txt", "r")
else:
    file = open("2025/inputi/day1.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

result = 50
count = 0

for line in lines:
    if line[0] == "L":
        result -= int(line[1:]) 
    elif line[0] == "R":
        result += int(line[1:]) 
    result %= 100
    if result == 0:
        count += 1
print(count)

print("***** PART 2 *****")

result = 50
count = 0

for line in lines:
    if line[0] == "L":
        for i in range(int(line[1:])):
            result -= 1
            result %= 100
            count += 1 if result == 0 else 0
    elif line[0] == "R":
        for i in range(int(line[1:])):
            result += 1
            result %= 100
            count += 1 if result == 0 else 0
print(count)
