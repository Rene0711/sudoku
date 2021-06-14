import numpy
from collections import Counter

def swordfish(values):

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
            if len(all_options[int(nmb)]) > 3 or len(all_options[int(nmb)]) < 2:
                del all_options[int(nmb)]
        for key, value in all_options.items():
            possible = dict()
            possible["option"] = key
            possible["value"] = value
            possible["line"] = l
            columns = []
            for v in value:
                columns.append(values[v].column)
            possible["column"] = columns
            all_possibles.append(possible)
    for possible in all_possibles:
        count = 0
        columns = []
        result_keys = []
        for search_possible in all_possibles:
            if possible["option"] == search_possible["option"]:
                count += 1
                columns = columns + search_possible["column"]
                result_keys = result_keys + search_possible["value"]
        if count == 3:
            option = possible["option"]
            columns = list(dict.fromkeys(columns))
            if len(columns) == 3:
                outside_keys = []

                for key, value in values.items():
                    for search_option in value.options:
                        if value.column in columns and key not in result_keys and option == search_option:
                            outside_keys.append(key)
                if len(outside_keys) > 0:
                    check = []
                    for result_key in result_keys:
                        check.append(result_key[0])
                    count_check = Counter(check)
                    for check_value in Counter(check):
                        if count_check[check_value] == 1:
                            return False, None, None
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
            if len(all_options[int(nmb)]) > 3 or len(all_options[int(nmb)]) < 2:
                del all_options[int(nmb)]
        for key, value in all_options.items():
            possible = dict()
            possible["option"] = key
            possible["value"] = value
            possible["column"] = c
            lines = []
            for v in value:
                lines.append(values[v].line)
            possible["line"] = lines
            all_possibles.append(possible)
    for possible in all_possibles:
        count = 0
        lines = []
        result_keys = []
        for search_possible in all_possibles:
            if possible["option"] == search_possible["option"]:
                count += 1
                lines = lines + search_possible["line"]
                result_keys = result_keys + search_possible["value"]
        if count == 3:
            option = possible["option"]
            lines = list(dict.fromkeys(lines))
            if len(lines) == 3:
                outside_keys = []

                for key, value in values.items():
                    for search_option in value.options:
                        if value.line in lines and key not in result_keys and option == search_option:
                            outside_keys.append(key)
                if len(outside_keys) > 0:
                    check = []
                    for result_key in result_keys:
                        check.append(result_key[1])
                    count_check = Counter(check)
                    for check_value in Counter(check):
                        if count_check[check_value] == 1:
                            return False, None, None
                    return result_keys, option, outside_keys

    return False, None, None