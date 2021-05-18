from sudoku.algorithms.helper.squares import square_finder


def find_empty(values):
    values_new_options = dict()
    for key, value in values.items():
        value.options = remove_column(values, value.options, value.column)
        value.options = remove_line(values, value.options, value.line)
        value.options = remove_square(values, value.options, value.square)

    return values


def remove_column(values, options, column):
    for key, value in values.items():
        if value.column == column:
            if value.value is not None:
                try:
                    options.remove(int(value.value))
                except:
                    pass
    return options


def remove_line(values, options, line):
    for key, value in values.items():
        if value.line == line:
            if value.value is not None:
                try:
                    options.remove(int(value.value))
                except:
                    pass
    return options


def remove_square(values, options, square):
    for key, value in values.items():
        if value.square == square:
            if value.value is not None:
                try:
                    options.remove(int(value.value))
                except:
                    pass
    return options


