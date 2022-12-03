with open('input.txt') as f:
    lines = f.read().splitlines()

import itertools

total = 0

for line in lines:
    c1, c2 = set(list(line[0:len(line)//2])), set(list(line[len(line)//2:]))
    common = list(c1.intersection(c2))[0]
    total += ord(common) - 96 if common.islower() else ord(common) - 38

print(total)

# Code Golf
print(sum(map(lambda c: ord(c) - 96 if c.islower() else ord(c) - 38, [next(iter(set(line[0:len(line)//2]) & set(line[len(line)//2:]))) for line in open('input.txt').read().splitlines()])))