from sudoku.algorithms.naked_single import naked_single
from sudoku.algorithms.hidden_single import hidden_single
from sudoku.algorithms.naked_pair import naked_pair
from sudoku.algorithms.helper.find_empty import find_empty


def solver(values):
    empty_options = False
    last_count = 0
    count = 0
    while (len(values) < 81):
        count_values = len(values)

        if not empty_options:
            empty_options = find_empty(values)

        values, empty_options = naked_single(values, empty_options)
        values, empty_options = hidden_single(values, empty_options)
        # values, empty_options = naked_pair(values, empty_options)

        if count_values == last_count:
            count = count + 1
            empty_options = False
            print("Mit den ausgewählten Algorithmen konnten nicht alle Zahlen ermittelt werden!")
            if count > 3:
                break
        else:
            count = 0

        last_count = len(values)

    return filled(values)


def filled(values):
    letters = "ABCDEFGHI"
    numbers = "123456789"

    for l in letters:
        for n in numbers:
            try:
                values[l + n]
            except:
                values[l + n] = ''
    return values


def values_to_objects(values):

    return values
