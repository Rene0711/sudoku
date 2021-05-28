from sudoku.algorithms.helper.squares import square_finder


def marked_area(values):
    column = []
    line = []

    for value in values:
        column.append(value[0])
        line.append(value[-1])

    if all(x == column[0] for x in column):
        numbers = "123456789"
        fields = []

        for n in numbers:
            fields.append(column[0] + n)

        return fields
    elif all(x == line[0] for x in line):
        letters = "ABCDEFGHI"
        fields = []

        for l in letters:
            fields.append(l + line[0])

        return fields

    else:
        return square_finder(values[0])
