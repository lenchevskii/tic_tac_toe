from numpy import diag
from modules.helpers import anti_diagonal, zip_split

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

WINNING_FUNCTIONS = [diag, anti_diagonal, zip_split]
