from random                 import choice
from modules.constants      import SIGN
from modules.grid_worker    import get_vacancies, get_win_combinations


def get_position(current, bot, grid):
    vacancies = get_vacancies(grid)
    if not vacancies:
        return print("DEAD HEAT")
    else:
        return int(input(f"Please, enter the vacant position for {SIGN[current]}\n"
                         f"(vacant positions have following indexes: "
                         f"{vacancies}): ")) \
            if bot == current else choice(vacancies)


def get_smart_position(grid):
    get_win_combinations(grid)