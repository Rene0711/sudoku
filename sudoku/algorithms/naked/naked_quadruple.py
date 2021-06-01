def naked_quadruple(values):
    found_keys, options, outside_keys = check_line(values)
    if found_keys is not False:
        return found_keys, options, outside_keys

    found_keys, options, outside_keys = check_column(values)
    if found_keys is not False:
        return found_keys, options, outside_keys

    found_keys, options, outside_keys = check_square(values)
    if found_keys is not False:
        return found_keys, options, outside_keys

    return False, None, None


def check_line(values):
    line = "123456789"

    for l in line:
        for key, value in values.items():
            if value.value is None and value.line is int(l) and len(value.options) == 4:
                options = value.options
                found_keys = [key]
                for search_key, search_value in values.items():
                    if search_value.value is None and search_value.line is int(l) and search_key is not key:
                        in_triple = True
                        for option in search_value.options:
                            if option not in options:
                                in_triple = False
                        if in_triple:
                            found_keys.append(search_key)
                if len(found_keys) == 4:
                    outside_keys = []
                    for outside_key, outside_value in values.items():
                        in_options = False
                        if outside_value.value is None and outside_value.line is int(l) and outside_key not in found_keys:
                            for option in outside_value.options:
                                if option in options:
                                    in_options = True
                            if in_options:
                                outside_keys.append(outside_key)
                    if len(outside_keys) > 0:
                        return found_keys, options, outside_keys
    return False, None, None


def check_column(values):
    column = "123456789"

    for c in column:
        for key, value in values.items():
            if value.value is None and value.column is int(c) and len(value.options) == 4:
                options = value.options
                found_keys = [key]
                for search_key, search_value in values.items():
                    if search_value.value is None and search_value.column is int(c) and search_key is not key:
                        in_triple = True
                        for option in search_value.options:
                            if option not in options:
                                in_triple = False
                        if in_triple:
                            found_keys.append(search_key)
                if len(found_keys) == 4:
                    outside_keys = []
                    for outside_key, outside_value in values.items():
                        in_options = False
                        if outside_value.value is None and outside_value.column is int(c) and outside_key not in found_keys:
                            for option in outside_value.options:
                                if option in options:
                                    in_options = True
                            if in_options:
                                outside_keys.append(outside_key)
                    if len(outside_keys) > 0:
                        return found_keys, options, outside_keys
    return False, None, None


def check_square(values):
    square = "123456789"

    for s in square:
        for key, value in values.items():
            if value.value is None and value.square is int(s) and len(value.options) == 4:
                options = value.options
                found_keys = [key]
                for search_key, search_value in values.items():
                    if search_value.value is None and search_value.square is int(s) and search_key is not key:
                        in_triple = True
                        for option in search_value.options:
                            if option not in options:
                                in_triple = False
                        if in_triple:
                            found_keys.append(search_key)
                if len(found_keys) == 4:
                    outside_keys = []
                    for outside_key, outside_value in values.items():
                        in_options = False
                        if outside_value.value is None and outside_value.square is int(
                                s) and outside_key not in found_keys:
                            for option in outside_value.options:
                                if option in options:
                                    in_options = True
                            if in_options:
                                outside_keys.append(outside_key)
                    if len(outside_keys) > 0:
                        return found_keys, options, outside_keys
    return False, None, None
