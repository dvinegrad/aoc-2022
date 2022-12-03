with open('input.txt') as f:
    lines = f.read().splitlines()

scores = {
    "X": { "A" : 4, "B" : 1, "C" : 7},
    "Y": { "A" : 8, "B" : 5, "C" : 2},
    "Z": { "A" : 3, "B" : 9, "C" : 6}
}

moves = [(line.split(' ')[0], line.split(' ')[1]) for line in lines]
total_score = sum([scores[move[1]][move[0]] for move in moves])
print(total_score)