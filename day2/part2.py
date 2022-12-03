with open('input.txt') as f:
    lines = f.read().splitlines()

scores = {
    "X": { "A" : 3, "B" : 1, "C" : 2},
    "Y": { "A" : 4, "B" : 5, "C" : 6},
    "Z": { "A" : 8, "B" : 9, "C" : 7}
}

moves = [(line.split(' ')[0], line.split(' ')[1]) for line in lines]
total_score = sum([scores[move[1]][move[0]] for move in moves])
print(total_score)