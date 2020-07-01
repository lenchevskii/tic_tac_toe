def all_equal(lst):
    return all(x == 'X' for x in lst) or all(x == '0' for x in lst)


def is_empty_position(lst, position):
    return lst[position] == '_'


def get_vacancies(lst):
    return [i for i, x in enumerate(lst) if x == '_']
