from sudoku.algorithms.helper.squares import square_finder


def find_empty(values):
    letters = "ABCDEFGHI"
    numbers = "123456789"
    empties = dict()
    fulls = dict()

    for l in letters:
        for n in numbers:
            try:
                fulls[l + n] = values[l + n]
            except:
                empties[l + n] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    return single_option(values, empties)


def remove_column(key, options, values):
    letter = key[0]
    numbers = "123456789"
    for n in numbers:
        if letter + n in values:
            try:
                options.remove(int(values[letter + n]))
            except:
                pass
    return options


def remove_line(key, options, values):
    letters = "ABCDEFGHI"
    number = key[-1]
    for l in letters:
        if l + number in values:
            try:
                options.remove(int(values[l + number]))
            except:
                pass
    return options


def remove_square(key, options, values):
    square = square_finder(key)
    for field in square:
        try:
            options.remove(int(values[field]))
        except:
            pass
    return options


def single_option(values, empties):
    for key, options in empties.items():
        options = remove_column(key, options, values)
        options = remove_line(key, options, values)
        options = remove_square(key, options, values)

    return empties
