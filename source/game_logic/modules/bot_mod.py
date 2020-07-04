from random                 import choice
from modules.constants      import SIGN
from modules.grid_worker    import get_vacancies


def get_position(current, bot, grid):
    vacancies = get_vacancies(grid)
    return int(input(f"Please, enter the vacant position for {SIGN[current]}\n"
                     f"(vacant positions have following indexes: "
                     f"{vacancies}): ")) \
        if bot != SIGN[current] else choice(vacancies)
