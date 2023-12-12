file = open("day1.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

sum = 0

for i in range(len(lines)):
    numeric_values = "".join([char for char in lines[i] if char.isdigit()])
    a = numeric_values[0] + numeric_values[-1]
    sum += int(a)

print("***** PART 1 *****")
print(sum)
print()

sum1 = 0
dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for i in range(len(lines)):
    a = ""
    for j in range(len(lines[i])):
        for word, number in dict.items():
            if lines[i][j:].startswith(word) or lines[i][j] == str(number):
                a += number
    a = a[0] + a[-1]
    sum1 += int(a)

print("***** PART 2 *****")
print(sum1)
