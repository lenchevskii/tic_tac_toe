from itertools import chain
from numpy import array_split, fliplr, matrix, diag

SIGN = '0' or 'X'

INITIAL_GRID = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

WINNING_COMBINATIONS = []


def anti_diagonal(arr):
    return list(fliplr(arr).diagonal())


def check_equal(lst):
    return all(x == 'X' for x in lst) or all(x == '0' for x in lst)


def chain_grid(grid):
    return list(chain.from_iterable(grid))


def update_sign(grid, sign, index):
    return grid[:index] + [sign] + grid[index + 1:]


def unchain_grid(lst):
    return list(map(list, array_split(lst, 3)))


def play(grid, sign: SIGN, position) -> SIGN:
    if not check_equal(anti_diagonal(grid)):
        new_grid = unchain_grid(update_sign(chain_grid(grid), sign, position))
        print(matrix(new_grid))
        new_position = int(input(f"Please, enter the position for {sign}: "))
        play(new_grid, sign, new_position)
    else:
        return print("X's win!")


if __name__ == "__main__":
    side = input("Choose X or 0 (hint: 'X' is the Dark Side): ").upper()
    initial_position = int(input(f"Please, enter the position for {side}: "))
    play(INITIAL_GRID, side, initial_position)
