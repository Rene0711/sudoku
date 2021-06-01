import numpy


def x_wing(values):
    found_keys, option, outside_keys = check_line(values)
    if found_keys is not False:
        return found_keys, option, outside_keys

    found_keys, options, outside_keys = check_column(values)
    if found_keys is not False:
        return found_keys, option, outside_keys

    return False, None, None


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
            if numpy.array_equal(possible["column"], search_possible["column"]) \
                    and possible["option"] is search_possible["option"] \
                    and possible["line"] is not search_possible["line"]:
                print("juhu")
                result_keys = possible["value"] + search_possible["value"]
                outside_keys = []
                for key, value in values.items():
                    if value.column in possible["column"] and key not in result_keys and value.value is None:
                        for option in value.options:
                            if option is possible["option"]:
                                outside_keys.append(key)
                if len(outside_keys) > 0:
                    return result_keys, possible["option"], outside_keys

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
            if numpy.array_equal(possible["line"], search_possible["line"]) \
                    and possible["option"] is search_possible["option"] \
                    and possible["column"] is not search_possible["column"]:
                print("juhu")
                result_keys = possible["value"] + search_possible["value"]
                outside_keys = []
                for key, value in values.items():
                    if value.line in possible["line"] and key not in result_keys and value.value is None:
                        for option in value.options:
                            if option is possible["option"]:
                                outside_keys.append(key)
                if len(outside_keys) > 0:
                    return result_keys, possible["option"], outside_keys

    return False, None, None


