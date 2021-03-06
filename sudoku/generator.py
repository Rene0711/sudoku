from random import randint, shuffle

counter = 1


def check_grid(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False

    return True


def solve_grid(grid):
    global counter
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            for value in range(1, 10):
                if not (value in grid[row]):
                    if not value in (
                            grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                            grid[6][col],
                            grid[7][col], grid[8][col]):
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if check_grid(grid):
                                counter += 1
                                break
                            else:
                                if solve_grid(grid):
                                    return True
            break
    grid[row][col] = 0


numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fill_grid(grid):
    global counter
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            shuffle(numberList)
            for value in numberList:
                if not (value in grid[row]):
                    if not value in (
                            grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                            grid[6][col],
                            grid[7][col], grid[8][col]):
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if check_grid(grid):
                                return True
                            else:
                                if fill_grid(grid):
                                    return True
            break
    grid[row][col] = 0


def handler(empty, diff):
    global counter
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    if not empty:
        attempts = int(diff)
        fill_grid(grid)

        while attempts > 0:
            row = randint(0, 8)
            col = randint(0, 8)
            while grid[row][col] == 0:
                row = randint(0, 8)
                col = randint(0, 8)
            backup = grid[row][col]
            grid[row][col] = 0

            copyGrid = []
            for r in range(0, 9):
                copyGrid.append([])
                for c in range(0, 9):
                    copyGrid[r].append(grid[r][c])

            counter = 0
            solve_grid(copyGrid)
            if counter != 1:
                grid[row][col] = backup
                attempts -= 1

    return grid


def get_grid(empty, diff):
    values = dict()
    grid = handler(empty, diff)
    count = 0
    count2 = 0

    for l in "ABCDEFGHI":
        for n in "123456789":
            value = grid[count][count2]
            if value == 0:
                values[l + n] = ''
            else:
                values[l + n] = grid[count][count2]
            count2 += 1
            if count2 == 9:
                count += 1
                count2 = 0

    return values
