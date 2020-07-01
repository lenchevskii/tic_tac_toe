from itertools import chain
from numpy import array_split


def chain_grid(grid):
    return list(chain.from_iterable(grid))


def update_sign(grid, sign, index):
    return grid[:index] + [sign] + grid[index + 1:]


def unchain_grid(lst, sections=3):
    return list(map(list, array_split(lst, sections)))
