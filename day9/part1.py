with open('input.txt') as f:
    steps = [(line.split(" ")[0], int(line.split(" ")[1])) for line in f.read().splitlines()]

def get_adjusted_tail(head, tail):
    diff = (head[0] - tail[0], head[1] - tail[1])

    if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
        return tail

    if abs(diff[0]) == 2:
        return ((tail[0] + head[0]) // 2, head[1])

    if abs(diff[1]) == 2:
        return (head[0], (tail[1] + head[1]) // 2)

ADJ = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}
 
visited = set()
head = (0, 0)
tail = (0, 0)

visited.add(tail)

for step in steps:
    direction = step[0]
    length = step[1]
    inc = ADJ[direction]

    for i in range(length):
        head = (head[0] + inc[0], head[1] + inc[1])
        
        tail = get_adjusted_tail(head, tail)
        visited.add(tail)

print(len(visited))

