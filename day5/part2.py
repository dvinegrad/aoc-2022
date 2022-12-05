import re

with open('input.txt') as f:
    initial_stacks, steps = f.read().split(" 1   2   3   4   5   6   7   8   9 \n\n")

stacks = [[] for i in range(9)]

for row in initial_stacks.splitlines():
    vals = [row[4 * i + 1] for i in range(9)]
    for i in range(len(vals)):
        if vals[i].isalpha():
            stacks[i].append(vals[i])

for stack in stacks:
    stack.reverse()

for step in steps.splitlines():
    m = re.match("move (\d+) from (\d+) to (\d+)", step)
    qty, s1, s2 = map(int, m.groups())
    stacks[s2 - 1].extend(stacks[s1 - 1][-qty:])
    del stacks[s1 - 1][-qty:]

res = "".join([s[-1] for s in stacks])
print(res)