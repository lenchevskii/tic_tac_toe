from modules.constants import SIGN


def all_equal(lst):
    return all(x == 'X' for x in lst) or all(x == '0' for x in lst)


def is_empty_position(lst, position):
    return lst[position] == '_'


def validate_sign(sing):
    return sing in SIGN


def validate_index(i):
    pass
