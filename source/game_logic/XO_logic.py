from modules.bot_mod        import get_position
from modules.constants      import SIGN, WINNING_FUNCTIONS
from modules.helpers        import pretty_matrix, flat_list
from modules.grid_worker    import update_grid, initiate_grid, enumerate_grid
from modules.validators     import all_equal, is_empty_position, validate_sign


def play(grid, sign, position, bot_sign):
    new_grid = update_grid(grid, sign, position)
    print(pretty_matrix(new_grid), "\n")
    winning_combinations = [all_equal(x) for x in
                            flat_list(y(new_grid) for y in WINNING_FUNCTIONS)]
    if not any(winning_combinations):
        new_position = get_position(sign, bot_sign, new_grid)
        print(f"New position for {SIGN[sign]}:", new_position)
        if is_empty_position(new_grid, new_position):
            play(new_grid, SIGN[sign], new_position, bot_sign)
        else:
            play(grid, sign, position, bot_sign)
    else:
        print(f"{sign}'s win!")


def infinite_start():
    n = int(input("Please, enter n for the grid (square matrix n×n):"))
    initial_grid = initiate_grid(n)
    print(f"\nTake a look at the Grid:\n\n"
          f"{pretty_matrix(enumerate_grid(initial_grid))}\n")
    human_side = input("Choose X or 0: ").upper()
    if not validate_sign(human_side):
        statement = input(
            "Luke, choose the correct side. Are you ready? (y/n): ").lower()
        if statement == 'n':
            return print("Bye!")
    else:
        robot_side = SIGN[human_side]
        print("Human sing:", human_side, "Bot:", robot_side)
        print("This is your palette:\n\n" + pretty_matrix(initial_grid) + "\n")
        initial_position = int(
            input(f"Please, enter the position for {human_side}: "))
        play(initial_grid, human_side, initial_position, robot_side)
    return infinite_start()


if __name__ == "__main__":
    infinite_start()

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
