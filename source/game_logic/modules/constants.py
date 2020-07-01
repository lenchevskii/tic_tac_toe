from numpy import diag
from modules.helpers import anti_diagonal, zip_split, noop
from modules.update_matrix import unchain_grid, chain_grid

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

GRID = unchain_grid(range(len(chain_grid(INITIAL_GRID))))

WINNING_FUNCTIONS = [diag, anti_diagonal, zip_split, noop]
