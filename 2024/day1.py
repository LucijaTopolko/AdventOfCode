file = open("2024/inputi/day1.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

sum = 0
left = []
right = []

for line in lines:
    l = line.split()
    left.append(int(l[0]))
    right.append(int(l[1]))

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    sum += abs(left[i] - right[i]) 

print(sum)

print("***** PART 2 *****")

sum = 0

for i in range(len(left)):
    a, b = left[i], 0
    for j in range(len(right)):
        if a == right[j]:
            b+=1
    sum+= a*b

print(sum)