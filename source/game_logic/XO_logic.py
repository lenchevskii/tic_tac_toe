from numpy import fliplr, matrix
from modules.helpers import all_equal, is_empty_position, get_vacancies
from modules.update_matrix import unchain_grid, update_sign, chain_grid

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

WINNING_COMBINATIONS = []


def anti_diagonal(arr):
    return list(fliplr(arr).diagonal())


def play(grid, sign, position):
    new_grid = unchain_grid(update_sign(chain_grid(grid), sign, position))
    print(matrix(new_grid), "\n")
    if not all_equal(anti_diagonal(new_grid)):
        new_position = int(input(f"Please, enter the vacant position for '{SIGN[sign]}'\n"
                                 f"Vacant positions have following indexes: {get_vacancies(chain_grid(new_grid))}): "))
        if is_empty_position(chain_grid(new_grid), new_position):
            play(new_grid, SIGN[sign], new_position)
        else:
            play(grid, sign, position)
    else:
        return print(f"{sign}'s win!")


if __name__ == "__main__":
    print("Let's start the game!\n", "\n", matrix(INITIAL_GRID), "\n")
    side = input("Choose X or 0 (hint: 'X' is the Dark Side): ").upper()
    initial_position = int(input(f"Please, enter the position for {side}: "))
    play(INITIAL_GRID, side, initial_position)


# Multiplayer
# def play(grid, sign, position):
#     new_grid = unchain_grid(update_sign(chain_grid(grid), sign, position))
#     print(matrix(new_grid))
#     if not all_equal(anti_diagonal(new_grid)):
#         new_position = int(input(f"Please, enter the vacant position for '{SIGN[sign]}'\n"
#                                  f"Vacant positions have following indexes: {get_vacancies(chain_grid(new_grid))}): "))
#         if is_empty_position(chain_grid(new_grid), new_position):
#             play(new_grid, SIGN[sign], new_position)
#         else:
#             play(grid, sign, position)
#     else:
#         return print(f"{sign}'s win!")
