class Monkey:
    def __init__(self, items, op, divisor, next_true, next_false):
        self.items = items
        self.op = op
        self.divisor = divisor
        self.next_true = next_true
        self.next_false = next_false
        self.inspected_count = 0

    def add_item(self, item):
        self.items.append(item)

    def execute_round(self, modulus):
        results = []
        for item in self.items:
            op_components = self.op.split(" ")
            val = item if op_components[2] == "old" else int(op_components[2])
            new_val = item + val if op_components[1] == "+" else item * val
            new_val %= modulus
            new_monkey = self.next_true if new_val % self.divisor == 0 else self.next_false
            results.append((new_val, new_monkey))
            self.inspected_count += 1
        
        self.items.clear()
        return results

    def get_inspected_count(self):
        return self.inspected_count

with open('input.txt') as f:
    lines = f.read().splitlines()

monkeys = []
modulus = 1

for i in range(0, len(lines), 7):
    items = [int(v) for v in lines[i + 1].split(": ")[1].split(", ")]
    op = lines[i + 2].split(" = ")[1]
    divisor = int(lines[i + 3].split(" ")[-1])
    modulus *= divisor
    next_true = int(lines[i + 4].split(" ")[-1])
    next_false = int(lines[i + 5].split(" ")[-1])
    monkeys.append(Monkey(items, op, divisor, next_true, next_false))

for i in range(10000):
    for m in monkeys:
        results = m.execute_round(modulus)
        for res in results:
            monkeys[res[1]].add_item(res[0])

vals = sorted(map(lambda m: m.get_inspected_count(), monkeys), reverse=True)

print(vals[0] * vals[1])