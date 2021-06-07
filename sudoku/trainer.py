from sudoku.algorithms.helper.find_empty import find_empty


def trainer(values, candidates):
    value_obj = find_empty(values_to_objects(filled(values), candidates))

    return objects_to_values(value_obj), objects_to_candidates(value_obj)


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
