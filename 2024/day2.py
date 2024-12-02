file = open("2024/inputi/input.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

def issafe(l):
    increasing = l[0] < l[1]
    for j in range(1, len(l)):
        if increasing and l[j - 1] >= l[j]:
            return False
        else:
            if not increasing and l[j-1] <= l[j]:
                return False
        if not 1 <= abs(l[j-1] - l[j]) <= 3:
            return False
    return True
    

print("***** PART 1 *****")

count = 0

for line in lines:
    l = list(map(int, line.split()))
    if issafe(l):
        count += 1

print(count)

print("***** PART 2 *****")

count = 0

for line in lines:
    l = list(map(int, line.split()))
    if issafe(l):
        count += 1
        continue

    for i in range(len(l)):
        temp = l[:i] + l[i+1:]
        if issafe(temp):
            count += 1
            break
    
print(count)