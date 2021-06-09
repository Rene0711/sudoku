from sudoku.algorithms.helper.squares import get_square


def string_kite(values):
    line = "123456789"
    column = "123456789"
    option_numbers = "123456789"

    all_line_possibles = []
    all_column_possibles = []

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
            all_line_possibles.append(possible)

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
            all_column_possibles.append(possible)

    for column_possible in all_column_possibles:
        for line_possible in all_line_possibles:
            if column_possible["option"] is line_possible["option"]:
                sqaure_count = 0
                square_values = []
                possible_values = []
                for col_value in column_possible["value"]:
                    possible_values.append(col_value)
                    col_value_square = get_square(col_value)
                    if col_value not in line_possible["value"]:
                        for line_value in line_possible["value"]:
                            possible_values.append(line_value)
                            line_value_square = get_square(line_value)
                            if col_value_square is line_value_square \
                                    and values[col_value].line is not values[line_value].line \
                                    and values[col_value].column is not values[line_value].column:
                                sqaure_count += 1
                                square_values.append(col_value)
                                square_values.append(line_value)
                    else:
                        sqaure_count += 10

                if sqaure_count == 1:
                    outside_values = list(dict.fromkeys(possible_values))
                    for possible_value in possible_values:
                        if possible_value in square_values:
                            try:
                                outside_values.remove(possible_value)
                            except:
                                pass
                    cut_fields = []
                    cut_fields.append(outside_values[0][0] + outside_values[1][-1])
                    cut_fields.append(outside_values[1][0] + outside_values[0][-1])

                    for cut_field in cut_fields:
                        if values[cut_field].value is None and column_possible["option"] in values[cut_field].options:
                            result_keys = square_values + outside_values
                            return result_keys, column_possible["option"], [cut_field]

    return False, None, None
