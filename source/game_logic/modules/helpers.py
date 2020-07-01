from numpy import fliplr
from modules.update_matrix import chain_grid


def all_equal(lst):
    return all(x == 'X' for x in lst) or all(x == '0' for x in lst)


def is_empty_position(lst, position):
    return lst[position] == '_'


def get_vacancies(lst):
    return [i for i, x in enumerate(lst) if x == '_']


def pretty_matrix(mtrx):
    return '\n'.join([' | '.join([cell for cell in row]) for row in mtrx])


def anti_diagonal(lst):
    return list(list(fliplr(lst).diagonal()))


def zip_split(lst):
    return [i[0] for i in zip(lst)]
