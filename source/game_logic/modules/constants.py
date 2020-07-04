from numpy              import diagonal, transpose
from modules.helpers    import anti_diagonal, noop


SIGN = {
    '0': 'X',
    'X': '0'
}

WINNING_FUNCTIONS = [diagonal, anti_diagonal, transpose, noop]
