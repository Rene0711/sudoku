from sudoku.algorithms.helper.squares import square_finder
from sudoku.algorithms.helper.find_empty import find_empty


def naked_single(values, old_empty_options):
    found = True
    while (found):
        if not old_empty_options:
            empty_options = find_empty(values)
        else:
            empty_options = old_empty_options
            old_empty_options = False
        count = False
        for key, options in empty_options.items():
            if len(options) == 1:
                count = True
                values[key] = str(options[0])
        if not count:
            found = False

    return values, empty_options