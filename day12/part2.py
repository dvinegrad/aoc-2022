def get_valid_neighbors(loc, n_rows, n_cols):
    return list(filter(lambda l: l[0] >= 0 and l[1] >= 0 and l[0] < n_rows and l[1] < n_cols, [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]))

def get_val(grid, loc):
    if grid[loc[0]][loc[1]] == 'S':
        return ord('a')
    elif grid[loc[0]][loc[1]] == 'E':
        return ord('z')
    else:
        return ord(grid[loc[0]][loc[1]])

def breadth_first_search(grid, start, end):
    n_rows = len(grid)
    n_cols = len(grid[0])

    visited = set()
    queue = []
    queue.append([start])

    while queue:
        cur = queue.pop(0)
        cur_loc = cur[-1]

        if cur_loc == end:
            return len(cur) - 1

        valid_neighbor_spots = get_valid_neighbors(cur[-1], n_rows, n_cols)
        for neighbor in filter(lambda l: get_val(grid, cur_loc) >= get_val(grid, l) - 1, valid_neighbor_spots):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(cur + [neighbor])

    return None



with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]

possible_starts = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S' or grid[i][j] == 'a':
            possible_starts.append((i, j))
        elif grid[i][j]  == 'E':
            end = (i, j)

best = min(filter(lambda x: x is not None, map(lambda start: breadth_first_search(grid, start, end), possible_starts)))
print(best)

