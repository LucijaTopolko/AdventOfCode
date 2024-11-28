from collections import Counter

file = open("day7.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

part1, part2 = 0, 0


def determine(hand, a):
    hand = hand.replace("T", chr(ord("9") + 1))
    hand = hand.replace("J", chr(ord("2") - 1) if a else chr(ord("9") + 2))  # ;
    hand = hand.replace("Q", chr(ord("9") + 3))
    hand = hand.replace("K", chr(ord("9") + 4))
    hand = hand.replace("A", chr(ord("9") + 5))

    C = Counter(hand)
    if a:
        target = list(C.keys())[0]
        for k in C:
            if k != "1":  # 1 je joker
                if C[k] > C[target] or target == "1":
                    target = k
        if "1" in C and target != "1":  # ako nam treba joker
            C[target] += C["1"]  # dodajemo najvećem joker
            del C["1"]  # brišemo joker

    if sorted(C.values()) == [5]:
        return (10, hand)
    elif sorted(C.values()) == [1, 4]:
        return (9, hand)
    elif sorted(C.values()) == [2, 3]:
        return (8, hand)
    elif sorted(C.values()) == [1, 1, 3]:
        return (7, hand)
    elif sorted(C.values()) == [1, 2, 2]:
        return (6, hand)
    elif sorted(C.values()) == [1, 1, 1, 2]:
        return (5, hand)
    elif sorted(C.values()) == [1, 1, 1, 1, 1]:
        return (4, hand)


pairs = []
for line in lines:
    hand, bid = line.split()
    pairs.append((hand, bid))

pairs = sorted(pairs, key=lambda pair: determine(pair[0], 0))

for i, (h, b) in enumerate(pairs, 0):
    part1 += (i + 1) * int(b)

print("***** PART 1 *****")
print(part1)
print()

pairs = []
for line in lines:
    hand, bid = line.split()
    pairs.append((hand, bid))
pairs = sorted(pairs, key=lambda hb: determine(hb[0], 1))

for i, (h, b) in enumerate(pairs, 0):
    part2 += (i + 1) * int(b)
print("***** PART 2 *****")
print(part2)
