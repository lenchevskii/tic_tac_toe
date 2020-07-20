from modules.constants 	    import SIGN
from modules.bot_mod 		import get_position, get_smart_position
from modules.grid_worker 	import update_grid, get_win_combinations, \
    initiate_grid, enumerate_grid
from modules.helpers 		import compose, pretty_matrix


def play_pipe(sign, grid, position, bot_sign):
    print(pretty_matrix(grid), "\n\n")
    if any(get_win_combinations(grid)):
        print(f"{sign}'s win!")
    else:
        play_pipe(
            SIGN[sign],
            update_grid(grid, sign, position),
            get_position(sign, bot_sign, update_grid(grid, sign, position)),
            bot_sign
        )


if __name__ == '__main__':
    n = int(input("Please, enter n for the grid (square matrix n×n):"))
    initial_grid = initiate_grid(n)
    print(f"\nTake a look at the Grid:\n\n"
          f"{pretty_matrix(enumerate_grid(initial_grid))}\n")
    human_side = input("Choose X or 0: ").upper()
    robot_side = SIGN[human_side]
    initial_pos = int(input(f"Please, enter the position for {human_side}: "))
    # play_pipe(human_side, initial_grid, initial_pos, robot_side)
    print(get_smart_position(initial_grid))
