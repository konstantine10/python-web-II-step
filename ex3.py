f = open("ex3.txt", "r")

seconds = int(f.readline())

input_grid = [row.split() for row in f]


def plant_bombs(grid, bomb_set):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                grid[i][j] = 'O'
                bomb_set.add((i, j))


def detonate_bombs(grid, bomb_set):
    for (i, j) in bomb_set:
        grid[i][j] = '.'
        if i > 0:
            grid[i - 1][j] = '.'
        if i < len(grid) - 1:
            grid[i + 1][j] = '.'
        if j > 0:
            grid[i][j - 1] = '.'
        if j < len(grid[0]) - 1:
            grid[i][j + 1] = '.'


def bomber_man(n, grid):
    newly_planted = set()
    old_planted = set()

    if n <= 2:
        return grid

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                old_planted.add((i, j))

    # simulation
    for sec in range(n + 1):
        if sec >= 3 and (sec % 2 == 1):
            detonate_bombs(grid, old_planted)
            old_planted = newly_planted
            newly_planted = set()

        elif sec >= 2 and (sec % 2 == 0):
            plant_bombs(grid, newly_planted)

    return [''.join(row) for row in grid]


print(bomber_man(seconds, input_grid))