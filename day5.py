import sys

lines = open("day5.txt").read().strip()

parts = lines.split("\n\n")
seeds, *maps = parts
seeds = seeds.split(":")[1].split()

part1, part2 = sys.maxsize, []


def pronadi(seed, x):
    rows = x.split("\n")[1:]
    pairs = [[int(a) for a in row.split()] for row in rows]
    for destination, source, range in pairs:
        if source <= int(seed) < source + range:
            return int(seed) + destination - source  # 79 + (52 - 50)
    return seed  # oni koji nisu mapirani


def pronadiUNizu(r, x):
    rows = x.split("\n")[1:]
    pairs = [[int(a) for a in row.split()] for row in rows]
    a = []
    for destination, source, range in pairs:
        endOfSource = source + range
        newRanges = []
        while r:
            (start, end) = r.pop()
            start = int(start)
            end = int(end)
            left = (start, min(end, source))  # seedovi manji od sourcea
            intersect = (
                max(start, source),
                min(end, endOfSource),
            )  # seedovi koji upadaju u ovu liniju (pairs)
            right = (max(start, endOfSource), end)  # seedovi veći od sourcea
            if left[1] > left[0]:  # u newRanges dodajemo one lijevo i dolje one desno
                newRanges.append(left)
            if (
                intersect[1] > intersect[0]
            ):  # u a dodajemo one koje smo pronašli u pairs s pravim novim brojem
                a.append(
                    (
                        intersect[0] + destination - source,
                        intersect[1] + destination - source,
                    )
                )
            if right[1] > right[0]:
                newRanges.append(right)

        r = newRanges  # to su oni za koje nema zapis pa ostaju isti sami sebi
    return a + r


for s in seeds:
    for x in maps:
        s = pronadi(s, x)
    part1 = min(part1, s)

print("***** PART 1 *****")
print(part1)
print()


pairsOfSeeds = list(zip(seeds[::2], seeds[1::2]))

for a, b in pairsOfSeeds:
    r = [(a, a + b)]  # range
    for x in maps:
        r = pronadiUNizu(r, x)
    part2.append(
        min(r)[0]
    )  # u r su prvi i zadnji element locationa, prvi< zadnjega pa gledamo samo prve elemente svakog rangea


print("***** PART 2 *****")
print(min(part2))
