import re

file = open("2024/inputi/day3.txt", "r")
lines = file.read()

print("***** PART 1 *****")

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, lines)
numbers = [(int(x), int(y)) for x, y in matches]

sum = sum(t[0] * t[1] for t in numbers)

print(sum)

print("***** PART 2 *****")

pattern = "mul\(\d+,\d+\)|do\(\)|don\'t\(\)"

matches = re.findall(pattern, lines)

sum = 0
do = True
for match in matches:
    if match == 'don\'t()':
        do = False
    elif match == 'do()':
        do = True
    elif do:
        a, b = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", match)[0]
        sum += int(a) * int(b)

print(sum)