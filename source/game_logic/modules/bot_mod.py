from itertools              import cycle
from random import choice

from modules.constants      import SIGN, BEST_MOVES
from modules.helpers        import get_vacancies
from modules.update_matrix  import chain_grid


def get_position(current, bot, grid):
    vacancies = get_vacancies(chain_grid(grid))
    return int(input(f"Please, enter the vacant position for {SIGN[current]}\n"
                     f"(vacant positions have following indexes: "
                     f"{vacancies}): ")) if bot != SIGN[current] else choice(vacancies)
