import json
from enum import Enum
from functools import cmp_to_key

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

def compare_for_sort(left, right):
    res = compare(left, right)
    if res == Result.LEFT:
        return -1
    elif res == Result.RIGHT:
        return 1
    else:
        return 0


with open('input.txt') as f:
    lines = f.read().splitlines()

packets = [[[2]], [[6]]]

for i in range(0, len(lines), 3):
    packets.append(json.loads(lines[i]))
    packets.append(json.loads(lines[i + 1]))


sorted_packets = sorted(packets, key=cmp_to_key(compare_for_sort))
idx1 = sorted_packets.index([[2]]) + 1
idx2 = sorted_packets.index([[6]]) + 1
print(idx1 * idx2)
