import itertools
import operator

file = open("2024/inputi/day7.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

def evaluate(values, comb):
    result = values[0]
    for i, op in enumerate(komb):
        result = operator_map[op](result, values[i+1])
    return result        

print("***** PART 1 *****")

sum = 0

operator_map = {
    '+': operator.add,
    '*': operator.mul
}

for line in lines:
    test, values = line.split(': ')
    values = list(map(int,values.split()))

    kombninacije = list(itertools.product("+*", repeat=len(values)-1))

    good = False
    for komb in kombninacije:
        if evaluate(values, komb) == int(test):
            good = True
    
    if good:
        sum += int(test)
        
print(sum)

print("***** PART 2 *****")

sum = 0

def concat(x, y):
    return int(f"{x}{y}")

operator_map['|'] = concat

for line in lines:
    test, values = line.split(': ')
    values = list(map(int,values.split()))

    kombninacije = list(itertools.product("+*|", repeat=len(values)-1))

    for komb in kombninacije:
        if evaluate(values, komb) == int(test):
            sum += int(test)
            break
        
print(sum)