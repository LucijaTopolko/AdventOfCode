file = open("2016/inputi/day3.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

count = 0

for line in lines:
  sides = list(map(int, line.split()))
  a, b, c = sides
  if a+b>c and a+c>b and b+c>a:
    count += 1

print(count)

print("***** PART 2 *****")

for i in range(len(lines)):
    lines[i] = list(map(int, lines[i].split()))

count = 0

i = 0
while i < len(lines):
  for j in range(3):
    a, b, c = lines[i][j], lines[i+1][j], lines[i+2][j]
    if a+b>c and a+c>b and b+c>a:
      count += 1
  i += 3

print(count)