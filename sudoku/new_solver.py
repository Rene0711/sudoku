from sudoku.algorithms.fish.swordfish import swordfish
from sudoku.algorithms.hidden.hidden_pair import hidden_pair
from sudoku.algorithms.intersections.locked_candidates_claiming import locked_candidates_claiming
from sudoku.algorithms.intersections.locked_candidates_pointing import locked_candidates_pointing
from sudoku.algorithms.naked.naked_pair import naked_pair
from sudoku.algorithms.naked.naked_quadruple import naked_quadruple
from sudoku.algorithms.naked.naked_triple import naked_triple
from sudoku.algorithms.single_digit_patterns.skyscraper import skyscraper
from sudoku.algorithms.single_digit_patterns.string_kite import string_kite
from sudoku.algorithms.singles.hidden_single import hidden_single
from sudoku.algorithms.singles.naked_single import naked_single
from sudoku.algorithms.fish.x_wing import x_wing

from sudoku.algorithms.helper.find_empty import find_empty
from sudoku.algorithms.helper.squares import get_square, square_finder
from sudoku.algorithms.helper.marked_area import marked_area_two, marked_area, marked_area_three
from sudoku.algorithms.uniqueness.unique_rectangle_one import unique_rectangle_one
from sudoku.algorithms.uniqueness.unique_rectangle_two import unique_rectangle_two


def solver(values, candidates):
    value_obj = find_empty(values_to_objects(filled(values), candidates))
    hints = dict()
    result_key = naked_single(value_obj)
    if result_key is not False:
        hints["1"] = ["Es ist ein Naked Single zu finden", "naked_single"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_key)]
        hints["3"] = ["Beachte das markierte Feld", str(result_key)]
        hints["4"] = ["In dieses Feld kommt markierter Wert", str(result_key), str(value_obj[result_key].options[0])]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)
    
    result_key, value = hidden_single(value_obj)
    if result_key is not False:
        hints["1"] = ["Es ist ein Hidden Single zu finden", "hidden_single"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_key)]
        hints["3"] = ["Beachte das markierte Feld", str(result_key)]
        hints["4"] = ["In dieses Feld kommt markierter Wert", str(result_key), value]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, value, outside_keys = locked_candidates_pointing(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Locked Candidates Type 1 (Pointing) zu finden", "locked_candidates_pointing"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_keys[0])]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, value, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, value, outside_keys = locked_candidates_claiming(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Locked Candidates Type 2 (Claiming) zu finden", "locked_candidates_claiming"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_keys[0])]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, value, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values, outside_keys = naked_pair(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Naked Pair zu finden", "naked_pair"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values, outside_keys = naked_triple(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Naked Triple zu finden", "naked_triple"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values, outside_keys = naked_quadruple(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Naked Quadruple zu finden", "naked_quadruple"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values = hidden_pair(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Hidden Pair zu finden", "hidden_pair"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values, outside_keys, house_type = x_wing(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein X-Wing zu finden", "x_wing"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, house_type)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values, outside_keys, house_type = swordfish(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Swordfish zu finden", "swordfish"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, house_type)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)
    
    result_keys, values, outside_keys, house_type = skyscraper(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Skyscraper zu finden", "skyscraper"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, house_type)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)
    
    result_keys, values, outside_keys = string_kite(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein 2-String Kite zu finden", "string_kite"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_three(result_keys)]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)

    result_keys, values, outside_keys = unique_rectangle_one(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Unique Rectangle Type 1 zu finden", "unique1"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, "column")]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
        return objects_to_values(value_obj), hints, objects_to_candidates(value_obj)
    

    result_keys, values, outside_keys, outside_values = unique_rectangle_two(value_obj)
    if result_keys is not False:
        hints["1"] = ["Es ist ein Unique Rectangle Type 2 zu finden", "unique2"]
        hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, "column")]
        hints["3"] = ["Beachte die markierten Felder", result_keys]
        hints["4"] = ["Die gr??nen Felder eleminieren die roten Felder", result_keys, values, outside_keys, outside_values]
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
    given_candidates = True

    for key, value in values.items():
        key_check = False
        if value is None:
            for c in "123456789":
                if candidates[key + "-" + c] != '':
                    key_check = True
        if key_check is False and value is None:
            given_candidates = False

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
