file = open("2017/inputi/day2.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

sum = 0

for line in lines:
  l = list(map(int, line.split()))
  sum += max(l) - min(l) 

print(sum)


print("***** PART 2 *****")

sum = 0

for line in lines:
  l = list(map(int, line.split()))
  for el in l:
    for el2 in l:
      if el != el2 and el % el2 == 0:
        sum += el // el2

print(sum)