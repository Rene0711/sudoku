from sudoku.algorithms.naked_single import naked_single
from sudoku.algorithms.hidden_single import hidden_single
from sudoku.algorithms.naked_pair import naked_pair
from sudoku.algorithms.helper.find_empty import find_empty
from sudoku.algorithms.helper.squares import get_square, square_finder


def solver(values):
    value_obj = find_empty(values_to_objects(filled(values)))
    hints = dict()

    result_key = naked_single(value_obj)
    if result_key is not False:
        hints["1"] = ["Es ist ein Naked Single zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_key)]
        hints["3"] = ["Beachte das markierte Feld", str(result_key)]
        hints["4"] = ["In dieses Feld kommt folgender Wert", str(result_key), str(value_obj[result_key].options[0])]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_key, value = hidden_single(value_obj)
    if result_key is not False:
        hints["1"] = ["Es ist ein Hidden Single zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_key)]
        hints["3"] = ["Beachte das markierte Feld", str(result_key)]
        hints["4"] = ["In dieses Feld kommt folgender Wert", str(result_key), value]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)


def filled(values):
    letters = "ABCDEFGHI"
    numbers = "123456789"

    for l in letters:
        for n in numbers:
            try:
                values[l + n]
            except:
                values[l + n] = None
    return values


class Field:
    def __init__(self, value, options, column, line, square):
        self.value = value
        self.options = options
        self.column = column
        self.line = line
        self.square = square


def values_to_objects(values):
    values_obj = dict()
    letters = "ABCDEFGHI"

    for key, value in values.items():
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if value is not None:
            options = []

        values_obj[key] = Field(value,
                                options,
                                letters.find(key[0]) + 1,
                                int(key[-1]),
                                get_square(key))

    return values_obj


def objects_to_values(values):
    values_plain = dict()

    for key, value in values.items():
        if value.value is None:
            values_plain[key] = ''
        else:
            values_plain[key] = value.value

    return values_plain


def objects_to_candidates(values):
    candidates_list = dict()

    for key, value in values.items():
        candidates_list[key] = value.options

    return candidates_list
