import numpy


def unique_rectangle_one(values):
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
                                        and numpy.array_equal(field_options, search_value.options) \
                                        and found_key is not search_key:

                                    found_column = search_key[0]
                                    found_line = values[search_key].line

                                    for other_line_key in found_keys:
                                        if values[other_line_key].line is not found_line:
                                            new_line = values[other_line_key].line

                                            outside_key = found_column + str(new_line)
                                            if all(numpy.isin(field_options, values[outside_key].options)) is True:
                                                found_keys.append(search_key)

                                                return found_keys, field_options, [outside_key]

    return False, None, None
