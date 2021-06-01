from sudoku.algorithms.hidden_pair import hidden_pair
from sudoku.algorithms.naked_quadruple import naked_quadruple
from sudoku.algorithms.naked_single import naked_single
from sudoku.algorithms.hidden_single import hidden_single
from sudoku.algorithms.locked_candidates_pointing import locked_candidates_pointing
from sudoku.algorithms.locked_candidates_claiming import locked_candidates_claiming
from sudoku.algorithms.naked_pair import naked_pair
from sudoku.algorithms.naked_triple import naked_triple
from sudoku.algorithms.x_wing import x_wing

from sudoku.algorithms.helper.find_empty import find_empty
from sudoku.algorithms.helper.squares import get_square, square_finder
from sudoku.algorithms.helper.marked_area import marked_area


def solver(values, candidates):
    value_obj = find_empty(values_to_objects(filled(values), candidates))
    hints = dict()
    """
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
    
    result_keys, value, outside_keys = locked_candidates_pointing(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Locked Candidates Type 1 (Pointing) zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_keys[0])]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, value, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, value, outside_keys = locked_candidates_claiming(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Locked Candidates Type 2 (Claiming) zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_keys[0])]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, value, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)
    
    result_keys, values, outside_keys = naked_pair(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Naked Pair zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values, outside_keys = naked_triple(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Naked Triple zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values, outside_keys = naked_quadruple(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Naked Quadruple zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values = hidden_pair(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Hidden Pair zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)
    """

    result_keys, values, outside_keys = x_wing(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein X-Wing zu finden"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)


    return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)


def filled(values):
    letters = "ABCDEFGHI"
    numbers = "123456789"

    for l in letters:
        for n in numbers:
            if values[l + n] == '':
                values[l + n] = None
    return values


class Field:
    def __init__(self, value, options, column, line, square):
        self.value = value
        self.options = options
        self.column = column
        self.line = line
        self.square = square


def values_to_objects(values, candidates):
    values_obj = dict()
    letters = "ABCDEFGHI"
    given_candidates = False

    for key, value in candidates.items():
        if value != '':
            given_candidates = True

    for key, value in values.items():
        options = []
        if value is None:
            if given_candidates:
                    for c in "123456789":
                        if candidates[key + "-" + c] != '':
                            options.append(int(candidates[key + "-" + c]))
            else:
                options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
