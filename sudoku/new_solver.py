from sudoku.algorithms.naked_single import naked_single
from sudoku.algorithms.hidden_single import hidden_single
from sudoku.algorithms.naked_pair import naked_pair
from sudoku.algorithms.helper.find_empty import find_empty


def solver(values):
    empty_options = False
    while(len(values) < 81):
        count_values = len(values)

        if not empty_options:
            empty_options = find_empty(values)

        values, empty_options = naked_single(values, empty_options)
        values, empty_options = hidden_single(values, empty_options)
        values, empty_options = naked_pair(values, empty_options)

        if count_values == len(values):
            print("Mit den ausgewählten Algorithmen konnten nicht alle Zahlen ermittelt werden!")
            break

    return values
