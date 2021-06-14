import numpy


def unique_rectangle_two(values):
    found_keys, field_options, outside_keys, outside_value = check_line(values)
    if found_keys is not False:
        return found_keys, field_options, outside_keys, outside_value

    found_keys, field_options, outside_keys, outside_value = check_column(values)
    if found_keys is not False:
        return found_keys, field_options, outside_keys, outside_value

    return False, None, None, None


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
                        for found_key in found_keys:
                            for search_key, search_value in values.items():
                                if values[found_key].column is search_value.column \
                                        and all(numpy.isin(field_options, search_value.options)) \
                                        and found_key is not search_key and len(search_value.options) == 3:
                                    check_options = search_value.options
                                    found_column = search_key[0]
                                    found_line = values[search_key].line
                                    outside_keys = []

                                    for other_line_key in found_keys:
                                        if other_line_key[0] is not found_column:
                                            new_column = other_line_key[0]
                                            new_key = new_column + str(found_line)

                                            if numpy.array_equal(values[new_key].options, check_options):
                                                found_keys.append(search_key)
                                                found_keys.append(new_key)
                                                outside_value = numpy.setdiff1d(check_options, field_options).tolist()[
                                                    0]

                                                for key, value in values.items():
                                                    if key not in found_keys and outside_value in value.options and (
                                                            value.line is values[search_key].line or value.column is
                                                            values[search_key].column or value.square is values[
                                                                search_key].square) and (
                                                            value.line is values[new_key].line or value.column is
                                                            values[new_key].column or value.square is values[
                                                                new_key].square):
                                                        outside_keys.append(key)
                                                if len(outside_keys) > 0:
                                                    return found_keys, field_options, outside_keys, outside_value

    return False, None, None, None


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
                        for found_key in found_keys:
                            for search_key, search_value in values.items():
                                if values[found_key].line is search_value.line \
                                        and all(numpy.isin(field_options, search_value.options)) \
                                        and found_key is not search_key and len(search_value.options) == 3:
                                    check_options = search_value.options
                                    found_column = search_key[0]
                                    found_line = values[search_key].line
                                    outside_keys = []

                                    for other_line_key in found_keys:
                                        if values[other_line_key].line is not found_line:
                                            new_line = values[other_line_key].line
                                            new_key = found_column + str(new_line)

                                            if numpy.array_equal(values[new_key].options, check_options):
                                                found_keys.append(search_key)
                                                found_keys.append(new_key)
                                                outside_value = numpy.setdiff1d(check_options, field_options).tolist()[
                                                    0]

                                                for key, value in values.items():
                                                    if key not in found_keys and outside_value in value.options and (
                                                            value.line is values[search_key].line or value.column is
                                                            values[search_key].column or value.square is values[
                                                                search_key].square) and (
                                                            value.line is values[new_key].line or value.column is
                                                            values[new_key].column or value.square is values[
                                                                new_key].square):
                                                        outside_keys.append(key)
                                                if len(outside_keys) > 0:
                                                    return found_keys, field_options, outside_keys, outside_value

    return False, None, None, None
