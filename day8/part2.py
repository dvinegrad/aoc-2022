def get_scenic_score(grid, i, j):
    val = grid[i][j]
    row = [grid[i][c] for c in range(len(grid))]
    col = [grid[r][j] for r in range(len(grid))]

    # if val > max(row[:j], default=-1) or val > max(row[j+1:], default=-1):
    #     return True

    # if val > max(col[:i], default=-1) or val > max(col[i+1:], default=-1):
    #     return True

    # return False
    up = 0
    down = 0
    left = 0
    right = 0

    for jj in range(j - 1, -1, -1):
        left += 1
        if row[jj] >= row[j]:
            break

    for jj in range(j + 1, len(grid)):
        right += 1
        if row[jj] >= row[j]:
            break

    for ii in range(i - 1, -1, -1):
        up += 1
        if col[ii] >= col[i]:
            break

    for ii in range(i + 1, len(grid)):
        down += 1
        if col[ii] >= col[i]:
            break

    return up * down * left * right
        

with open('input.txt') as f:
    lines = f.read().splitlines()

grid = [[int(v) for v in line] for line in lines]

scenic_max = 0

for i in range(len(grid)):
    for j in range(len(grid)):
        scenic_max = max(get_scenic_score(grid, i, j), scenic_max)

print(scenic_max)