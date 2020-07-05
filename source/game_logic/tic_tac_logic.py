from modules.bot_mod        import get_position
from modules.grid_worker    import update_grid, get_win_combinations
from modules.helpers        import compose


def play_pipe(sign, grid, position, mod):
    return compose(
        [get_win_combinations, get_position, update_grid]
    )(sign, grid, position, mod)
