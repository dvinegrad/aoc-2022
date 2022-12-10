with open('input.txt') as f:
    instructions = f.read().splitlines()

cycle = 1
x = 1
signal_strength = 0
i = 0
deferred_val = None

while True:
    if (cycle - 20) % 40 == 0:
        signal_strength += x * cycle

    if deferred_val is not None:
        cycle += 1
        x += deferred_val
        deferred_val = None

    elif i < len(instructions):
        instr = instructions[i]

        if instr == "noop":
            cycle += 1
        else:
            deferred_val = int(instr.split(" ")[1])
            cycle += 1
        i += 1
    else:
        break

print(signal_strength)



