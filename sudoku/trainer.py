import sudoku.generator
from sudoku.algorithms.fish.x_wing import x_wing
from sudoku.algorithms.helper.find_empty import find_empty
from sudoku.algorithms.helper.marked_area import marked_area, marked_area_two, marked_area_three
from sudoku.algorithms.helper.squares import get_square, square_finder
from sudoku.algorithms.hidden.hidden_pair import hidden_pair
from sudoku.algorithms.intersections.locked_candidates_claiming import locked_candidates_claiming
from sudoku.algorithms.intersections.locked_candidates_pointing import locked_candidates_pointing
from sudoku.algorithms.naked.naked_pair import naked_pair
from sudoku.algorithms.naked.naked_quadruple import naked_quadruple
from sudoku.algorithms.naked.naked_triple import naked_triple
from sudoku.algorithms.single_digit_patterns.skyscraper import skyscraper
from sudoku.algorithms.single_digit_patterns.string_kite import string_kite
from sudoku.algorithms.singles.hidden_single import hidden_single
from sudoku.algorithms.singles.naked_single import naked_single
from sudoku.algorithms.uniqueness.unique_rectangle_one import unique_rectangle_one


def trainer(name):
    title = ''
    description = ''
    hints = dict()

    if name == 'naked_single':
        title = 'Naked Single'
        description = 'Ein Naked Single ist eine Ziffer die in einem bestimmten Feld der einzige Kandidat ist. Diese ' \
                      'Ziffer muss in der Zelle gesetzt werden.'
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_key = naked_single(value_obj)
        if result_key is not False:
            hints["1"] = ["Es ist ein Naked Single zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_key)]
            hints["3"] = ["Beachte das markierte Feld", str(result_key)]
            hints["4"] = ["In dieses Feld kommt folgender Wert", str(result_key), str(value_obj[result_key].options[0])]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'hidden_single':
        title = 'Hidden Single'
        description = 'Ein Hidden Single bezeichnet eine Ziffer die in einem beliebigen Haus nur noch einen ' \
                      'bestimmten Platz einnehmen kann. Allerdings ist diese Art von Single versteckt zwischen ' \
                      'anderen möglichen Kandidaten. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_key, value = hidden_single(value_obj)
        if result_key is not False:
            hints["1"] = ["Es ist ein Hidden Single zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_key)]
            hints["3"] = ["Beachte das markierte Feld", str(result_key)]
            hints["4"] = ["In dieses Feld kommt folgender Wert", str(result_key), value]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'locked_candidates_pointing':
        title = 'Locked Candidates Type 1 (Pointing)'
        description = 'Ein Locked Candidate ist, wenn innerhalb eines Blocks alle Kandidaten einer Ziffer auf eine ' \
                      'bestimmte Reihe oder Spalte reduziert werden kann. Diese Ziffer kann somit in der kompletten ' \
                      'Reihe oder Spalte nicht mehr vorkommen und gestrichen werden. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, value, outside_keys = locked_candidates_pointing(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Locked Candidates Type 1 (Pointing) zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_keys[0])]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, value, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'locked_candidates_claiming':
        title = 'Locked Candidates Type 2 (Claiming)'
        description = 'Ein Locked Candidate ist, wenn innerhalb eines Blocks alle Kandidaten einer Ziffer auf eine ' \
                      'bestimmte Reihe oder Spalte reduziert werden kann. Diese Ziffer kann somit in der kompletten ' \
                      'Reihe oder Spalte nicht mehr vorkommen und gestrichen werden. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, value, outside_keys = locked_candidates_claiming(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Locked Candidates Type 2 (Claiming) zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", square_finder(result_keys[0])]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, value, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'naked_pair':
        title = 'Naked Pair'
        description = 'Wenn man zwei Zellen im selben Haus finden kann, die beide nur noch die selben zwei Kandidaten '\
                      'übrig haben, kann man diese Kandidaten aus allen anderen Zellen des Hauses löschen. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys = naked_pair(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Naked Pair zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'naked_triple':
        title = 'Naked Triple'
        description = 'Kann man in einem Haus drei Zellen finden, die nur noch die selben Kandidaten übrig haben, ' \
                      'kann man diese Kandidaten aus allen anderen Zellen dieses Hauses entfernen. Wichtig ist dabei, '\
                      'dass nicht alle Zellen alle Kandidaten enthalten müssen, aber in allen drei Zellen zusammen ' \
                      'dürfen insgesamt nicht mehr als drei verschiedene Kandidaten sein. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys = naked_triple(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Naked Triple zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'naked_quadruple':
        title = 'Naked Quadruple'
        description = 'Naked Quadruples funktionieren gleich wie Naked Triples und Naked Pairs, nur werden jetzt vier '\
                      'Kandidaten in vier Zellen benötigt. Da eine Schnittmenge zwischen einer Zeile und einem Block ' \
                      'oder zwischen einer Spalte und einem Block maximal drei Zellen haben kann, kann es kein Locked '\
                      'Quadruple geben. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys = naked_quadruple(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Naked Quadruple zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'hidden_pair':
        title = 'Hidden Pair'
        description = 'Wenn man zwei Zellen in ' \
                      'einem Haus finden kann, so dass zwei der Kandidaten in diesen Zellen nirgendwo sonst innerhalb '\
                      'des Hauses vorkommen können, müssen diese beiden Ziffern in diesen beiden Zellen gesetzt ' \
                      'werden. Alle anderen Kandidaten können aus diesen Zellen gelöscht werden. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values = hidden_pair(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Hidden Pair zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area(result_keys)]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'x_wing':
        title = 'X-Wing'
        description = 'Man nehme zwei Zeilen (die Base-Sets). Wenn es gelingt zwei Spalten zu finden, so dass alle ' \
                      'Kandidaten einer bestimmten Ziffer (der Fischziffer) aus beiden Zeilen in den Spalten (den ' \
                      'Cover-Sets) enthalten sind, können alle Fischkandidaten, die nicht in den Zeilen enthalten ' \
                      'sind, aus den Spalten gelöscht werden. Das ganze Muster wird X-Wing in den Zeilen genannt. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys, house_type = x_wing(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein X-Wing zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, house_type)]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'string_kite':
        title = '2-String Kite'
        description = 'Wenn wir eine Zeile und eine Spalte finden können, die nur noch zwei Kandidaten der Ziffer ' \
                      'enthalten (die Schnüre des Drachens), so dass ein Kandidat der Zeile und ein Kandidat der ' \
                      'Spalte sich im selben Block befinden, dann kann der Kandidat, der die beiden anderen Enden der ' \
                      'Schnüre sieht, gelöscht werden. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys = string_kite(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein 2-String Kite zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_three(result_keys)]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'skyscraper':
        title = 'Skyscraper'
        description = 'Die Beschreibung des Musters klingt komplizierter als es eigentlich ist: Man konzentriert sich '\
                      'auf eine Ziffer. Nun versucht man zwei Zeilen (Spalten) zu finden, die nur noch je zwei ' \
                      'Kandidaten für die Ziffer haben. Sind zwei dieser Kandidaten in derselben Spalte (Zeile), ' \
                      'muss einer der beiden anderen wahr sein. Alle Kandidaten, die diese beiden Zellen sehen, ' \
                      'können gelöscht werden. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys, house_type = skyscraper(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Skyscraper zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, house_type)]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'unique1':
        title = 'Unique Rectangle Type 1'
        description = 'Ein UR Typ 1 existiert, wenn genau eine Zelle eines möglichen URs zusätzliche Kandidaten hat. ' \
                      'Würden diese Kandidaten gelöscht, würde das UR existieren und zwei Lösungen bewirken. Es ist ' \
                      'daher absolut notwendig einen der zusätzlichen Kandidaten zu setzen. Das bedeutet, ' \
                      'dass die UR-Kandidaten aus dieser Zelle gelöscht werden können. '
        values = sudoku.generator.get_grid(False, 1)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys = unique_rectangle_one(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Unique Rectangle Type 1 zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, "column")]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    values = sudoku.generator.get_grid(False, 1)
    value_obj = find_empty(values_to_objects(filled(values)))
    return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)


def filled(values):
    letters = "ABCDEFGHI"
    numbers = "123456789"

    for l in letters:
        for n in numbers:
            if values[l + n] == '':
                values[l + n] = None
    return values


class Field:
    def __init__(self, value, options, column, line, square):
        self.value = value
        self.options = options
        self.column = column
        self.line = line
        self.square = square


def values_to_objects(values):
    values_obj = dict()
    letters = "ABCDEFGHI"

    for key, value in values.items():
        options = []
        if value is None:
            options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        values_obj[key] = Field(value,
                                options,
                                letters.find(key[0]) + 1,
                                int(key[-1]),
                                get_square(key))

    return values_obj


def objects_to_values(values):
    values_plain = dict()

    for key, value in values.items():
        if value.value is None:
            values_plain[key] = ''
        else:
            values_plain[key] = value.value

    return values_plain


def objects_to_candidates(values):
    candidates_list = dict()

    for key, value in values.items():
        candidates_list[key] = value.options

    return candidates_list
