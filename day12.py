from functools import lru_cache

file = open("day12.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]


@lru_cache
def count(sequence, springs):
    if len(springs) == 0:
        if "#" not in sequence:
            return 1
        else:
            return 0
    if len(sequence) == 0:
        return 0

    next_char = sequence[0]
    next_spring = springs[0]

    def demaged():
        s = sequence[:next_spring].replace("?", "#")
        if s != next_spring * "#":
            return 0
        elif len(sequence) == next_spring:
            if len(springs) == 1:
                return 1
            else:
                return 0
        elif (
            sequence[next_spring] in ".?"
        ):  # mora biti jer inače su dvije grupe spojene
            return count(sequence[next_spring + 1 :], springs[1:])
        return 0

    def operational():
        return count(sequence[1:], springs)

    if next_char == "#":
        out = demaged()
    elif next_char == ".":
        out = operational()
    else:
        out = operational() + demaged()
    return out


part1, part2 = 0, 0

for line in lines:
    sequence, springs = line.split(" ")
    springs = [int(i) for i in springs.split(",")]
    part1 += count(sequence, tuple(springs))
    sequence = "?".join([sequence] * 5)
    springs = springs * 5
    part2 += count(sequence, tuple(springs))

print("***** PART 1 *****")
print(part1)
print()

print("***** PART 2 *****")
print(part2)
