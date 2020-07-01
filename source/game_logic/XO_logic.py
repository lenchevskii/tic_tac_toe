from modules.constants import SIGN, INITIAL_GRID, WINNING_FUNCTIONS, GRID
from modules.helpers import get_vacancies, pretty_matrix
from modules.update_matrix import unchain_grid, update_sign, chain_grid
from modules.validators import all_equal, is_empty_position, validate_sign


# Single-player
def play(grid, sign, position):
    new_grid = unchain_grid(update_sign(chain_grid(grid), sign, position))
    print(pretty_matrix(new_grid), "\n")
    winning_combinations = [all_equal(x) for x in
                            unchain_grid(chain_grid([chain_grid(x(new_grid)) for x in WINNING_FUNCTIONS]), 8)]
    if not any(winning_combinations):
        new_position = int(input(f"Please, enter the vacant position for {SIGN[sign]}\n"
                                 f"(vacant positions have following indexes: {get_vacancies(chain_grid(new_grid))}): "))
        if is_empty_position(chain_grid(new_grid), new_position):
            play(new_grid, SIGN[sign], new_position)
        else:
            play(grid, sign, position)
    else:
        return print(f"{sign}'s win!")


if __name__ == "__main__":
    while True:
        print("\nLet's start the game!\nTake a look at the Grid:\n\n" + pretty_matrix(GRID) + "\n")
        side = input("Choose X or 0: ").upper()
        if validate_sign(side):
            print("This is your palette:\n\n" + pretty_matrix(INITIAL_GRID) + "\n")
            initial_position = int(input(f"Please, enter the position for {side}: "))
            play(INITIAL_GRID, side, initial_position)
        else:
            statement = input("Luke, choose the correct side. Are you ready? (y/n): ").lower()
            if statement == 'n':
                break

# Multi-player
"""
def play(grid, sign, position):
    new_grid = unchain_grid(update_sign(chain_grid(grid), sign, position))
    print(pretty_matrix(new_grid), "\n")
    winning_combinations = [all_equal(x) for x in
                            unchain_grid(chain_grid([chain_grid(x(new_grid)) for x in WINNING_FUNCTIONS]), 8)]
    if not any(winning_combinations):
        new_position = int(input(f"Please, enter the vacant position for {SIGN[sign]}\n"
                                 f"(vacant positions have following indexes: {get_vacancies(chain_grid(new_grid))}): "))
        if is_empty_position(chain_grid(new_grid), new_position):
            play(new_grid, SIGN[sign], new_position)
        else:
            play(grid, sign, position)
    else:
        return print(f"{sign}'s win!")
"""
