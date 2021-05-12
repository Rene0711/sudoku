from sudoku.algorithms.helper.squares import square_finder


def naked_pair(values, empty_options):
    if len(values) == 81:
        return values, empty_options
    else:
        for key, option in empty_options.items():
            square = square_finder(key)



    # Schritt 1 möglichen Wert picken
    # Schritt 2 schauen ob im Feld (Zeile oder Spalte) der Wert erneut auftritt
    # Schritt 3 Wenn ja, dann schauen ob wert außerhalb der Zeile oder Spalte auftritt
    # Schritt 4 für diese Zeile die möglichen Werte löschen

    return values, empty_options

