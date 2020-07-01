from itertools              import cycle
from modules.constants      import SIGN, BEST_MOVES
from modules.helpers        import get_vacancies
from modules.update_matrix  import chain_grid


def get_position(current, bot, grid):
    return int(input(f"Please, enter the vacant position for {SIGN[current]}\n"
                     f"(vacant positions have following indexes: "
                     f"{get_vacancies(chain_grid(grid))}): ")) if bot != current else next(cycle(BEST_MOVES))
