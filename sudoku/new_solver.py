from sudoku.algorithms.naked_single import naked_single
from sudoku.algorithms.hidden_single import hidden_single


def solver(values):
    values = naked_single(values)

    return values
