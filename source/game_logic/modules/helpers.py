from functools  import reduce
from numpy      import fliplr, ndarray
from itertools  import chain


def pretty_matrix(mtrx):
    return '\n\n'.join([' | '.join([str(cell).center(len(mtrx) // 2)
                                    for cell in row]) for row in mtrx])


def anti_diagonal(lst):
    return list(list(fliplr(lst).diagonal()))


def noop(item):
    return item


# [[e1], [e2], [[e3], [e4], [e5]], ... [en]] ->
#               -> [[e1], [e2], [e3], [e4], [e5], ... [en]]
# where e3, e4 or e5 is instance of ...
def flat_list(lst):
    return list(chain.from_iterable(
        [map(list, i)
         if any(map(lambda x: isinstance(x, ndarray)
                              or isinstance(x, list), i))
         else [list(i)] for i in lst]
    ))


def compose(*fns):
    return reduce(lambda f, g: lambda x: f(g(x)), fns,
                  lambda a, b, c, d: [a, b, c, d])
