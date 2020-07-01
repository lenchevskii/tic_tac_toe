from numpy                  import diag
from modules.helpers        import anti_diagonal, zip_split, noop
from modules.update_matrix  import unchain_grid, chain_grid

# dictionary for fast switch
SIGN = {
    '0': 'X',
    'X': '0'
}

INITIAL_GRID = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]

GRID = unchain_grid(range(len(chain_grid(INITIAL_GRID))))

WINNING_FUNCTIONS = [diag, anti_diagonal, zip_split, noop]
