import collections

import numpy


def skyscraper(values):
    found_keys, option, outside_keys = check_line(values)
    if found_keys is not False:
        return found_keys, option, outside_keys, "line"

    found_keys, option, outside_keys = check_column(values)
    if found_keys is not False:
        return found_keys, option, outside_keys, "column"

    return False, None, None, None


def check_line(values):
    line = "123456789"
    option_numbers = "123456789"

    all_possibles = []

    for l in line:
        all_options = dict()
        for nmb in option_numbers:
            all_options[int(nmb)] = []
        for key, value in values.items():
            if value.value is None and value.line is int(l):
                for option in value.options:
                    count = all_options[option]
                    all_options[option] = count + [key]
        for nmb in option_numbers:
            if len(all_options[int(nmb)]) != 2:
                del all_options[int(nmb)]
        for key, value in all_options.items():
            possible = dict()
            possible["option"] = key
            possible["value"] = value
            possible["line"] = l
            possible["column"] = [values[value[0]].column, values[value[1]].column]
            all_possibles.append(possible)

    for possible in all_possibles:
        for search_possible in all_possibles:
            if possible["option"] is search_possible["option"] \
                    and possible["line"] is not search_possible["line"] \
                    and not numpy.array_equal(possible["column"], search_possible["column"]):
                duplicate = False
                for possible_column in possible["column"]:
                    if possible_column in search_possible["column"]:
                        duplicate = True

                if duplicate:
                    option = possible["option"]
                    result_keys = possible["value"] + search_possible["value"]
                    result_key_columns = possible["column"] + search_possible["column"]
                    double_column = [item for item, count in collections.Counter(result_key_columns).items() if
                                     count > 1]
                    result_key_squares = []
                    remove_keys = []
                    for result_key in result_keys:
                        result_key_squares.append(values[result_key].square)

                        if values[result_key].column not in double_column:
                            remove_keys.append(result_key)

                    if len(result_key_squares) == len(set(result_key_squares)):
                        outside_keys = []
                        for key, value in values.items():
                            if option in value.options \
                                    and (value.line is values[remove_keys[0]].line or value.column is values[
                                    remove_keys[0]].column or value.square is values[remove_keys[0]].square) \
                                    and (value.line is values[remove_keys[1]].line or value.column is values[
                                    remove_keys[1]].column or value.square is values[remove_keys[1]].square):
                                outside_keys.append(key)
                        if len(outside_keys) > 0:
                            return result_keys, option, outside_keys

    return False, None, None


def check_column(values):
    column = "123456789"
    option_numbers = "123456789"

    all_possibles = []

    for c in column:
        all_options = dict()
        for nmb in option_numbers:
            all_options[int(nmb)] = []
        for key, value in values.items():
            if value.value is None and value.column is int(c):
                for option in value.options:
                    count = all_options[option]
                    all_options[option] = count + [key]
        for nmb in option_numbers:
            if len(all_options[int(nmb)]) != 2:
                del all_options[int(nmb)]
        for key, value in all_options.items():
            possible = dict()
            possible["option"] = key
            possible["value"] = value
            possible["column"] = c
            possible["line"] = [values[value[0]].line, values[value[1]].line]
            all_possibles.append(possible)

    for possible in all_possibles:
        for search_possible in all_possibles:
            if possible["option"] is search_possible["option"] \
                    and possible["column"] is not search_possible["column"] \
                    and not numpy.array_equal(possible["line"], search_possible["line"]):
                duplicate = False
                for possible_column in possible["line"]:
                    if possible_column in search_possible["line"]:
                        duplicate = True

                if duplicate:
                    option = possible["option"]
                    result_keys = possible["value"] + search_possible["value"]
                    result_key_line = possible["line"] + search_possible["line"]
                    double_line = [item for item, count in collections.Counter(result_key_line).items() if
                                   count > 1]
                    result_key_squares = []
                    remove_keys = []
                    for result_key in result_keys:
                        result_key_squares.append(values[result_key].square)

                        if values[result_key].line not in double_line:
                            remove_keys.append(result_key)

                    if len(result_key_squares) == len(set(result_key_squares)):
                        outside_keys = []
                        for key, value in values.items():
                            if option in value.options \
                                    and (value.line is values[remove_keys[0]].line or value.column is values[
                                    remove_keys[0]].column or value.square is values[remove_keys[0]].square) \
                                    and (value.line is values[remove_keys[1]].line or value.column is values[
                                    remove_keys[1]].column or value.square is values[remove_keys[1]].square):
                                outside_keys.append(key)
                        if len(outside_keys) > 0:
                            return result_keys, option, outside_keys

    return False, None, None
