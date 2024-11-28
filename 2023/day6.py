with open("day6.txt", "r") as file:
    lines = file.readlines()

times = list(map(int, lines[0].split()[1:]))
distance = list(map(int, lines[1].split()[1:]))

part1 = 1

for i in range(len(times)):
    part1 *= sum(1 for j in range(times[i]) if distance[i] < (j * (times[i] - j)))

print("***** PART 1 *****")
print(part1)
print()

t = int("".join(map(str, times)))
d = int("".join(map(str, distance)))
part2 = sum(1 for j in range(t) if d < (j * (t - j)))

print("***** PART 2 *****")
print(part2)
