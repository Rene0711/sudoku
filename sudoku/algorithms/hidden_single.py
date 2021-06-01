def hidden_single(values):
    for key, value in values.items():
        if value.value is None:
            for option in value.options:
                column = check_column(key, value.column, option, values)
                if column is not False:
                    return key, option
                line = check_line(key, value.line, option, values)
                if line is not False:
                    return key, option
                square = check_square(key, value.square, option, values)
                if square is not False:
                    return key, option
    return False, None


def check_column(search_key, column, search_option, values):
    for key, value in values.items():
        if value.column is column and search_key is not key:
            for option in value.options:
                if option is search_option:
                    return False
    return search_option


def check_line(search_key, line, search_option, values):
    for key, value in values.items():
        if value.line is line and search_key is not key:
            for option in value.options:
                if option is search_option:
                    return False
    return search_option


def check_square(search_key, square, search_option, values):
    for key, value in values.items():
        if value.square is square and search_key is not key:
            for option in value.options:
                if option is search_option:
                    return False
    return search_option
