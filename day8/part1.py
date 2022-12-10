def is_visible(grid, i, j):
    val = grid[i][j]
    row = [grid[i][c] for c in range(len(grid))]
    col = [grid[r][j] for r in range(len(grid))]

    if val > max(row[:j], default=-1) or val > max(row[j+1:], default=-1):
        return True

    if val > max(col[:i], default=-1) or val > max(col[i+1:], default=-1):
        return True

    return False

with open('input.txt') as f:
    lines = f.read().splitlines()

grid = [[int(v) for v in line] for line in lines]

ct = 0

for i in range(len(grid)):
    for j in range(len(grid)):
        if is_visible(grid, i, j):
            ct += 1

print(ct)