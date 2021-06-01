import numpy


def naked_pair(values):
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
        fields = []
        for key, value in values.items():
            if value.value is None and value.line is int(l) and len(value.options) == 2:
                fields.append(key)
        if len(fields) >= 2:
            for field in fields:
                for search_field in fields:
                    field_options = values[field].options
                    search_field_options = values[search_field].options
                    if field is not search_field and numpy.array_equal(field_options, search_field_options):
                        found_keys = [field, search_field]
                        outside_keys = []
                        for search_key, search_value in values.items():
                            if search_value.line is int(l) and search_key not in found_keys:
                                for search_value_option in search_value.options:
                                    if search_value_option in field_options:
                                        outside_keys.append(search_key)

                        if len(outside_keys) > 0:
                            return found_keys, field_options, list(dict.fromkeys(outside_keys))

    return False, None, None


def check_column(values):
    column = "123456789"

    for c in column:
        fields = []
        for key, value in values.items():
            if value.value is None and value.column is int(c) and len(value.options) == 2:
                fields.append(key)
        if len(fields) >= 2:
            for field in fields:
                for search_field in fields:
                    field_options = values[field].options
                    search_field_options = values[search_field].options
                    if field is not search_field and numpy.array_equal(field_options, search_field_options):
                        found_keys = [field, search_field]
                        outside_keys = []
                        for search_key, search_value in values.items():
                            if search_value.column is int(c) and search_key not in found_keys:
                                for search_value_option in search_value.options:
                                    if search_value_option in field_options:
                                        outside_keys.append(search_key)

                        if len(outside_keys) > 0:
                            return found_keys, field_options, list(dict.fromkeys(outside_keys))

    return False, None, None


def check_square(values):
    square = "123456789"

    for s in square:
        fields = []
        for key, value in values.items():
            if value.value is None and value.square is int(s) and len(value.options) == 2:
                fields.append(key)
        if len(fields) >= 2:
            for field in fields:
                for search_field in fields:
                    field_options = values[field].options
                    search_field_options = values[search_field].options
                    if field is not search_field and numpy.array_equal(field_options, search_field_options):
                        found_keys = [field, search_field]
                        outside_keys = []
                        for search_key, search_value in values.items():
                            if search_value.square is int(s) and search_key not in found_keys:
                                for search_value_option in search_value.options:
                                    if search_value_option in field_options:
                                        outside_keys.append(search_key)

                        if len(outside_keys) > 0:
                            return found_keys, field_options, list(dict.fromkeys(outside_keys))

    return False, None, None
