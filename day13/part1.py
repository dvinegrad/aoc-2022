import json
from enum import Enum 

class Result(Enum):
    LEFT = 1
    RIGHT = 2
    CONTINUE = 3

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return Result.LEFT
        elif left > right:
            return Result.RIGHT
        else:
            return Result.CONTINUE

    if type(left) == list and type(right) == list:
        for i in range(min(len(left), len(right))):
            res = compare(left[i], right[i])
            if res != Result.CONTINUE:
                return res
            
        if len(left) < len(right):
            return Result.LEFT
        elif len(left) > len(right):
            return Result.RIGHT
        else:
            return Result.CONTINUE

    if type(left) == int:
        return compare([left], right)
    else:
        return compare(left, [right])

with open('input.txt') as f:
    lines = f.read().splitlines()

total = 0

for i in range(0, len(lines), 3):
    left = json.loads(lines[i])
    right = json.loads(lines[i + 1])
    if compare(left, right) == Result.LEFT:
        total += (i // 3) + 1

print(total)