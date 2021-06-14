import sudoku.generator
from sudoku.algorithms.fish.swordfish import swordfish
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
from sudoku.algorithms.uniqueness.unique_rectangle_two import unique_rectangle_two


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
            hints["4"] = ["In dieses Feld kommt markierter Wert", str(result_key),
                          str(value_obj[result_key].options[0])]
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
            hints["4"] = ["In dieses Feld kommt markierter Wert", str(result_key), value]
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
        description = 'Der zweite Typ des Locked Candidates ist genau umgekehrt wie der Erste. Wenn in einer Reihe ' \
                      'oder Spalte alle Kandidaten einer Ziffer auf genau einen Block beschränkt sind, so können alle ' \
                      'Kandidaten dieser Ziffer aus dem jeweiligen Block entfernt werden. '
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
        description = 'Naked Subsets sind Felder in den sowohl die gleiche Anzahl von Kandidaten als auch die selben ' \
                      'Werte der Kandidaten Platz finden. Beim Beispiel des Naked Pairs befinden sich zwei gleiche ' \
                      'Kandidaten in genau zwei Feldern einer Reihe, Spalte oder Blocks. '
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
        description = 'Das Naked Triple ist genau gleich wie das Naked Pair, jedoch handelt es sich um drei ' \
                      'Kandidaten auf drei verschiedenen Feldern einer Reihe, Spalte oder Blocks. '
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
        description = 'Das Naked Quadruple findet dann Anwendung, wenn vier Kandidaten sich vier Felder teilen und ' \
                      'keine weiteren Kandidaten in diesen Feldern möglich sind. '
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
        description = 'Beim Hidden Pair sucht man zwei Zellen eines Hauses die zwei Kandidaten ' \
                      'besitzen, die sonst in keiner Zelle des Hauses Platz finden. Die beiden Ziffern müssen somit ' \
                      'in diesen beiden Zellen Platz finden und somit können alle weiteren Kandidaten der beiden ' \
                      'Zellen entfernt werden. '
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
        description = 'Ein X-Wing, auch Kreuzflügler genannt, ist eine Fisch Strategie. Man findet einen X-Wing indem ' \
                      'man nach zwei Reihen oder Spalten sucht wo ein Kandidat nur zwei verschiedene mögliche Felder ' \
                      'besitzt. Nun hat man vier Felder in denen der Kandidat möglich ist, wenn diese Felder ein ' \
                      'Rechteck bilden hat man ein X-Wing gefunden. Denn es gibt nur zwei Möglichkeiten in welche ' \
                      'zwei der vier Kandidaten gesetzt werden und diese Möglichkeiten kann man sich wie die Arme ' \
                      'eines Kreuzes vorstellen. Entweder die Kandidaten rechts oben und links unten oder links oben ' \
                      'und rechts unten werden gesetzt. Egal welche der beiden Möglichkeiten eintritt, in keiner der ' \
                      'Reihe oder Spalten kann sonst noch ein Kandidat der gleichen Ziffer auftreten. '
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
        description = 'Ein 2-String Kite gehört in die Kategorie der Single Digit Patterns. Man kann ihn finden, ' \
                      'indem man eine Ziffer sucht, deren Kandidaten nur noch zwei mögliche Kandidaten in einer Zeile ' \
                      'und einer Spalte aufweisen. Eine weitere Bedingung ist, dass sich ein Kandidat der Zeile und ' \
                      'einer der Spalte in dem selben Block befinden muss. Wenn das der Fall ist kann der Kandidat ' \
                      'der beide Enden (die nicht im selben Block sind) sieht entfernt werden, denn eines der beiden ' \
                      'Enden muss wahr sein. '
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
        description = 'Ein Skyscraper ist ähnlich wie die X-Wing Strategie, jedoch bilden die vier Felder kein ' \
                      'Rechteck. Bei einem Skyscraper sucht man denselben Kandidaten, der in zwei Reihen oder Spalten ' \
                      'genau zwei Möglichkeiten aufweist. Wenn dann auch noch zwei dieser Kandidaten zusätzlich in ' \
                      'der selben Reihe oder Spalte sind spricht man von einem Skyscraper. Eine der anderen beiden ' \
                      'Kandidaten muss folglich wahr sein und es können alle Kandidaten aus den Zellen entfernt ' \
                      'werden, die diese beiden Zellen sehen. '
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
        description = 'Ein Unique Rectangle hat vier Felder in genau zwei Rehen, zwei Spalten und zwei Blöcken. In ' \
                      'jedem der vier Felder stehen dieselben zwei Kandidaten. Da viele Sudoku Spieler der Meinung ' \
                      'sind, dass ein Sudoku nur eine Lösung besitzt, versucht man Unique Rectangles zu vermeiden. ' \
                      'Denn in dem Moment wo ein, wie oben beschrieben, Unique Rectangle auftaucht hat das Sudoku ' \
                      'zwei Lösungen und ist somit nicht mehr eindeutig. Die unterschiedlichen Types versuchen das zu ' \
                      'vermeiden. '
        values = sudoku.generator.get_grid(False, 1)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys = unique_rectangle_one(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Unique Rectangle Type 1 zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, "column")]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'unique2':
        title = 'Unique Rectangle Type 2'
        description = 'Der zweite Typ des Unique Rectangle versucht wie der erste ein zweideutiges Sudoku zu ' \
                      'verhindern. Der einzige Unterschied ist, dass nun zwei Kandidaten desselben Werts in nicht ' \
                      'diagonalen Zellen des UR existieren. Um das UR zu vermeiden wird einer dieser Kandidaten ' \
                      'sicher gesetzt werden und daher können alle Kandidaten desselben Wertes, die von ihnen gesehen ' \
                      'werden eliminiert werden. '
        values = sudoku.generator.get_grid(False, 3)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys, outside_values = unique_rectangle_two(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Unique Rectangle Type 2 zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, "column")]
            hints["3"] = ["Beachte die markierten Felder", result_keys]
            hints["4"] = ["Die grünen Felder eleminieren die roten Felder", result_keys, values, outside_keys,
                          outside_values]
            return objects_to_values(value_obj), hints, title, description, objects_to_candidates(value_obj)

    if name == 'swordfish':
        title = 'Swordfish'
        description = 'Ein Swordfish funktioniert genau gleich wie ein X-Wing. Der einzige Unterschied ist, dass der ' \
                      'Swordfish drei Base-Sets und drei Cover-Sets besitzt. Base-Sets sind Häuser die sich nicht ' \
                      'überschneiden und in ihnen befinden sich die Basis Kandidaten. Unter nicht überschneiden ' \
                      'versteht man, dass die Basis Kandidaten in nur einem Haus vorkommen dürfen. Die Cover-Sets ' \
                      'sind Häuser die alle Basis Kandidaten abdecken, in ihnen befinden sich die Cover-Kandidaten. '
        values = sudoku.generator.get_grid(False, 5)
        value_obj = find_empty(values_to_objects(filled(values)))
        result_keys, values, outside_keys, house_type = swordfish(value_obj)
        if result_keys is not False:
            hints["1"] = ["Es ist ein Swordfish zu finden"]
            hints["2"] = ["Es ist im markierten Bereich zu finden", marked_area_two(result_keys, house_type)]
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
