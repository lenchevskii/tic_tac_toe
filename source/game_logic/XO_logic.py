from functools import reduce

from modules.constants import SIGN, INITIAL_GRID, WINNING_FUNCTIONS
from modules.helpers import all_equal, is_empty_position, get_vacancies, pretty_matrix, zip_split, anti_diagonal
from modules.update_matrix import unchain_grid, update_sign, chain_grid


# Single-player
def play(grid, sign, position):
    new_grid = unchain_grid(update_sign(chain_grid(grid), sign, position))
    print(pretty_matrix(new_grid), "\n")
    winning_combinations = map(new_grid, WINNING_FUNCTIONS)
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
    # print("Let's start the game!\n" + "\n" + pretty_matrix(INITIAL_GRID) + "\n")
    # side = input("Choose X or 0 (hint: 'X' is the Dark Side): ").upper()
    # initial_position = int(input(f"Please, enter the position for {side}: "))
    # play(INITIAL_GRID, side, initial_position)
    winning_combinations = list(map(lambda x: list(x(INITIAL_GRID)), WINNING_FUNCTIONS))
    print(winning_combinations)


# Multi-player
"""def play(grid, sign, position):
    new_grid = unchain_grid(update_sign(chain_grid(grid), sign, position))
    print(pretty_matrix(new_grid))
    if not all_equal(anti_diagonal(new_grid)):
        new_position = int(input(f"Please, enter the vacant position for '{SIGN[sign]}'\n"
                                 f"Vacant positions have following indexes: {get_vacancies(chain_grid(new_grid))}): "))
        if is_empty_position(chain_grid(new_grid), new_position):
            play(new_grid, SIGN[sign], new_position)
        else:
            play(grid, sign, position)
    else:
        return print(f"{sign}'s win!")
"""