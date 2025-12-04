USE_TEST = 0

if USE_TEST:
    file = open("2018/inputi/day1_test.txt", "r")
else:
    file = open("2018/inputi/day1.txt", "r")

lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

freq = 0

for line in lines:
    freq += int(line)

print(freq)

print("***** PART 2 *****")

def find_dup_freq():
    freq = 0
    frequences = set()
    frequences.add(freq)
    while True:
        for line in lines:
            freq += int(line)
            if freq in frequences:
                return freq
            frequences.add(freq)

print(find_dup_freq())