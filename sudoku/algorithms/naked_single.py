from sudoku.algorithms.helper.find_empty import find_empty


def naked_single(values):
    for key, value in values.items():
        if len(value.options) == 1:
            return key
    return False
