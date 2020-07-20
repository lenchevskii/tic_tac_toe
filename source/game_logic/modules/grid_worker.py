from itertools          import chain
from numpy              import array_split, full
from modules.constants  import WINNING_FUNCTIONS
from modules.helpers    import flat_list
from modules.validators import all_equal


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


def enumerate_grid(grid):
    return unchain_grid(range(len(chain_grid(grid))), len(grid))


def get_vacancies(grid):
    return [i for i, x in enumerate(chain_grid(grid)) if x == '_']


def get_win_combinations(grid):
    return [all_equal(x) for x in flat_list(y(grid) for y in WINNING_FUNCTIONS)]


def is_empty_position(grid, position):
    return chain_grid(grid)[position] == '_'
