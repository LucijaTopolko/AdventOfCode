USE_TEST = 0

if USE_TEST:
    file = open("2025/inputi/day3_test.txt", "r")
else:
    file = open("2025/inputi/day3.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

sum = 0

for line in lines:
    maximum = max(line)
    if maximum == line[-1]:
        a = False
        for i in line[:-1]:
            if i == maximum:
                a = True
        if not a:
            maximum_2 = maximum
            maximum = max(line[:-1])
        else: 
            maximum_2 = max(line[line.index(maximum)+1:])
    else:
        maximum_2 = max(line[line.index(maximum)+1:])
    sum += int(maximum+maximum_2)

print(sum)

print("***** PART 2 *****")

sum = 0

for line in lines:
    seq = ''
    index = -1
    for i in range(13,1, -1):
        a = line[index+1:(len(line)-i+2)]
        seq += max(a)
        index = index + a.index(max(a)) + 1
    sum += int(seq)

print(sum)
