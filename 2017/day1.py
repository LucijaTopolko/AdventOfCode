file = open("2017/inputi/day1.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

lines = lines[0]
print("***** PART 1 *****")

sum = 0
length = len(lines)

for i in range(length):
  if lines[i] == lines[(i+1) % length]:
    sum += int(lines[i])

print(sum)


print("***** PART 2 *****")

count = 0

for i in range(length):
  if lines[i] == lines[(i + length//2) % length]:
    count += int(lines[i])

print(count)