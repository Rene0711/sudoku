import numpy


def hidden_pair(values):
    found_keys, options = check_line(values)
    if found_keys is not False:
        return found_keys, options

    found_keys, options = check_column(values)
    if found_keys is not False:
        return found_keys, options

    found_keys, options = check_square(values)
    if found_keys is not False:
        return found_keys, options

    return False, None


def check_line(values):
    line = "123456789"
    option_numbers = "123456789"

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
        for ao_key, ao_value in all_options.items():
            for sao_key, sao_value in all_options.items():
                if sao_key is not ao_key and numpy.array_equal(ao_value, sao_value):
                    removable = False
                    for aos_value in ao_value:
                        if len(values[aos_value].options) > 2:
                            removable = True
                    if removable:
                        return sao_value, [ao_key, sao_key]

    return False, None


def check_column(values):
    column = "123456789"
    option_numbers = "123456789"

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
        for ao_key, ao_value in all_options.items():
            for sao_key, sao_value in all_options.items():
                if sao_key is not ao_key and numpy.array_equal(ao_value, sao_value):
                    removable = False
                    for aos_value in ao_value:
                        if len(values[aos_value].options) > 2:
                            removable = True
                    if removable:
                        return sao_value, [ao_key, sao_key]

    return False, None


def check_square(values):
    square = "123456789"
    option_numbers = "123456789"

    for s in square:
        all_options = dict()
        for nmb in option_numbers:
            all_options[int(nmb)] = []
        for key, value in values.items():
            if value.value is None and value.square is int(s):
                for option in value.options:
                    count = all_options[option]
                    all_options[option] = count + [key]
        for nmb in option_numbers:
            if len(all_options[int(nmb)]) != 2:
                del all_options[int(nmb)]
        for ao_key, ao_value in all_options.items():
            for sao_key, sao_value in all_options.items():
                if sao_key is not ao_key and numpy.array_equal(ao_value, sao_value):
                    removable = False
                    for aos_value in ao_value:
                        if len(values[aos_value].options) > 2:
                            removable = True
                    if removable:
                        return sao_value, [ao_key, sao_key]

    return False, None
