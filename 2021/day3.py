USE_TEST = 0

if USE_TEST:
    file = open("2021/inputi/day3_test.txt", "r")
else:
    file = open("2021/inputi/day3.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

def most_common(lines, i):
    cnt0, cnt1 = 0, 0
    for line in lines:
        if line[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
    if cnt0 > cnt1:
        return '0'
    return '1'

print("***** PART 1 *****")

gamma = ""
epsilon = ""

for i in range(len(lines[0])):
    cnt0, cnt1 = 0, 0
    gamma += most_common(lines, i)
    epsilon += '1' if gamma[-1] == '0' else '0'

gamma_decimal = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma_decimal * epsilon)

print("***** PART 2 *****")

oxygen = lines.copy()

for i in range(len(lines[0])):
    g = most_common(oxygen, i)
    oxygen = [line for line in oxygen if line[i] == g]
    if len(oxygen) == 1:
        break

oxygen_decimal = int(oxygen[0], 2)

co2 = lines.copy()
for i in range(len(lines[0])):
    g = most_common(co2, i)
    co2 = [line for line in co2 if line[i] != g]
    if len(co2) == 1:
        break

co2_decimal = int(co2[0], 2)

print(oxygen_decimal * co2_decimal)