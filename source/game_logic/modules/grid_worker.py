from itertools  import chain
from numpy import array_split, full


def chain_grid(grid):
    return list(chain.from_iterable(grid))


# immutable list update
def update_sign(grid, sign, index):
    return grid[:index] + [sign] + grid[index + 1:]


def unchain_grid(lst, sections):
    return list(map(list, array_split(lst, sections)))


def update_grid(grid, sign, position):
    return unchain_grid(update_sign(chain_grid(grid), sign, position), len(grid))


def initiate_grid(n):
    return full((n, n), '_')


def enumerate_grid(lst):
    return unchain_grid(range(len(chain_grid(lst))), len(lst))
