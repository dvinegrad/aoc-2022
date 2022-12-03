with open('input.txt') as f:
    lines = f.read().splitlines()

total = 0

groups = [[set(l) for l in lines[i:i+3]] for i in range(0, len(lines), 3)]
for group in groups:
    common = next(iter(group[0].intersection(group[1]).intersection(group[2])))
    total += ord(common) - 96 if common.islower() else ord(common) - 38

print(total)

# Code Golf
print(sum(map(lambda c: ord(c) - 96 if c.islower() else ord(c) - 38, next(map(lambda lines: [next(iter(group[0] & group[1] & group[2])) for group in [[set(l) for l in lines[i:i+3]] for i in range(0, len(lines), 3)]], [open('input.txt').read().splitlines()])))))