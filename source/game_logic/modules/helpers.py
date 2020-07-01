from numpy import fliplr


def get_vacancies(lst):
    return [i for i, x in enumerate(lst) if x == '_']


def pretty_matrix(mtrx):
    return '\n'.join([' | '.join([str(cell) for cell in row]) for row in mtrx])


def anti_diagonal(lst):
    return list(list(fliplr(lst).diagonal()))


def zip_split(lst):
    a, b, c = [i[0] for i in zip(lst)]
    return a, b, c


def noop(item):
    return item
