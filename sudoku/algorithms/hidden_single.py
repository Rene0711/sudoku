from sudoku.algorithms.helper.squares import square_finder


def hidden_single(values, empty_options):
    if len(values) == 81:
        return values, empty_options
    else:
        for key, option in empty_options.items():
            column_result = column_check(key, empty_options)
            if column_result:
                values[key] = str(column_result)
                return values, empty_options
            else:
                line_result = line_check(key, empty_options)
                if line_result:
                    values[key] = str(line_result)
                    return values, empty_options
                else:
                    square_result = square_check(key, empty_options)
                    if square_result:
                        values[key] = str(square_result)
                        return values, empty_options
    return values, empty_options


def column_check(key, empty_options):
    letter = key[0]
    numbers = "123456789"

    for option in empty_options[key]:
        doubled = False
        for n in numbers:
            try:
                for other_option in empty_options[letter + n]:
                    if other_option == option:
                        if key != letter + n:
                            doubled = True
            except:
                pass
        if not doubled:
            return option
    return False


def line_check(key, empty_options):
    letters = "ABCDEFGHI"
    number = key[-1]
    options = []

    for option in empty_options[key]:
        doubled = False
        for l in letters:
            try:
                for other_option in empty_options[l + number]:
                    if other_option == option:
                        if key != l + number:
                            doubled = True
            except:
                pass
        if not doubled:
            return option
    return False


def square_check(key, empty_options):
    square = square_finder(key)

    for option in empty_options[key]:
        for field in square:
            try:
                for other_option in empty_options[field]:
                    if other_option == option:
                        if key != field:
                            doubled = True
            except:
                pass
        if not doubled:
            return option
    return False
