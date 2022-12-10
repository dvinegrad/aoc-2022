with open('input.txt') as f:
    steps = [(line.split(" ")[0], int(line.split(" ")[1])) for line in f.read().splitlines()]

def get_adjusted_tail(head, tail):
    diff = (head[0] - tail[0], head[1] - tail[1])

    if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
        return tail

    if abs(diff[0]) == 2:
        if diff[1] == 0:
            return ((tail[0] + head[0]) // 2, head[1])
        else:
            return (tail[0] + diff[0] // abs(diff[0]), tail[1] + diff[1] // abs(diff[1]))

    if abs(diff[1]) == 2:
        if diff[0] == 0:
            return (head[0], (tail[1] + head[1]) // 2)
        else:
            return (tail[0] + diff[0] // abs(diff[0]), tail[1] + diff[1] // abs(diff[1]))

ADJ = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}
 
visited = set()
knots = [(0, 0) for i in range(10)]

visited.add(knots[-1])

for step in steps:
    direction = step[0]
    length = step[1]
    inc = ADJ[direction]

    for i in range(length):
        knots[0] = (knots[0][0] + inc[0], knots[0][1] + inc[1])
        
        for i in range(9):
            knots[i+1] = get_adjusted_tail(knots[i], knots[i+1])
        
        visited.add(knots[-1])

print(len(visited))

