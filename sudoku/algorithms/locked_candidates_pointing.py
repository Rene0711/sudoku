def locked_candidates_pointing(values):
    for key, value in values.items():
        if value.value is None:
            for option in value.options:
                line_check, found_keys, outside_keys = check_line(option, key, values)
                if line_check is not False:
                    return found_keys, option, outside_keys

                column_check, found_keys, outside_keys = check_column(option, key, values)
                if column_check is not False:
                    return found_keys, option, outside_keys
    return False, None, None


def check_line(option, key, values):
    line = values[key].line
    square = values[key].square
    found = False
    outside = False
    found_keys = []
    outside_keys = []

    for search_key, value in values.items():
        if search_key is not key and value.line is line and value.square is square:
            for search_option in value.options:
                if search_option is option:
                    found = True
                    found_keys.append(search_key)
        elif search_key is not key and value.line is not line and value.square is square:
            for search_option in value.options:
                if search_option is option:
                    return False, None, None
        elif search_key is not key and value.line is line and value.square is not square:
            for search_option in value.options:
                if search_option is option:
                    outside = True
                    outside_keys.append(search_key)

    if outside:
        found_keys.append(key)
        return found, found_keys, outside_keys
    else:
        return False, None, None


def check_column(option, key, values):
    column = values[key].column
    square = values[key].square
    found = False
    outside = False
    found_keys = []
    outside_keys = []

    for search_key, value in values.items():
        if search_key is not key and value.column is column and value.square is square:
            for search_option in value.options:
                if search_option is option:
                    found = True
                    found_keys.append(search_key)
        elif search_key is not key and value.column is not column and value.square is square:
            for search_option in value.options:
                if search_option is option:
                    return False, None, None
        elif search_key is not key and value.column is column and value.square is not square:
            for search_option in value.options:
                if search_option is option:
                    outside = True
                    outside_keys.append(search_key)

    if outside:
        found_keys.append(key)
        return found, found_keys, outside_keys
    else:
        return False, None, None
