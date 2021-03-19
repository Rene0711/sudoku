
import copy
import time
import os


def solved(values):
    for u in values:
        if len(values[u]) < 1:
            return -1
        elif len(values[u]) > 1:
            return 0
    return 1


def clear():
    if __name__ == "__main__":
        os.system('cls' if os.name == 'nt' else 'clear')


class Solver(object):

    def __init__(self, input):
        self.letters = "ABCDEFGHI"
        self.numbers = "123456789"

        self.rows = dict()
        for l in self.letters:
            row = list()
            for n in self.numbers:
                row.append(l + n)
            for u in row:
                self.rows[u] = row

        self.columns = dict()
        for n in self.numbers:
            column = list()
            for l in self.letters:
                column.append(l + n)
            for u in column:
                self.columns[u] = column

        self.boxes = dict()
        for r in range(0, 3):
            for c in range(0, 3):
                box = list()
                for l in range(0, 3):
                    for n in range(0, 3):
                        box.append(self.letters[l+3*r] + self.numbers[n+3*c])
                for u in box:
                    self.boxes[u] = box

        self.values = dict()
        for l in self.letters:
            for n in self.numbers:
                self.values[l + n] = "123456789"

        self.parse(input)

        self.start_time = time.time()
        self.values = self.solve(self.values)

        if self.values:
            clear()
        else:
            print("The puzzle was not solvable")

    def parse(self, input):
        for key in input:
            if input[key] in "123456789":
                for u in self.rows[key]:
                    if u != key and u in input and input[u] == input[key]:
                        self.values = False
                        return
                for u in self.columns[key]:
                    if u != key and u in input and input[u] == input[key]:
                        self.values = False
                        return
                for u in self.boxes[key]:
                    if u != key and u in input and input[u] == input[key]:
                        self.values = False
                        return
            self.assign(self.values, key, input[key])

    def remove(self, values, key, value):
        if value not in values[key]:
            return

        values[key] = values[key].replace(value, "")

        if len(values[key]) == 1:
            self.assign(values, key, values[key])

        for i in range(1, 10):
            self.single(values, self.rows, key, str(i))
            self.single(values, self.columns, key, str(i))
            self.single(values, self.boxes, key, str(i))

    def assign(self, values, key, value):
        if value not in values[key]:
            return

        remove = values[key].replace(value, "")
        for r in remove:
            self.remove(values, key, r)

        for u in self.rows[key]:
            if not u == key:
                self.remove(values, u, value)
        for u in self.columns[key]:
            if not u == key:
                self.remove(values, u, value)
        for u in self.boxes[key]:
            if not u == key:
                self.remove(values, u, value)

    def single(self, values, group, key, value):
        candidates = list()
        for u in group[key]:
            if value in values[u]:
                candidates.append(u)
        if len(candidates) == 1 and len(values[candidates[0]]) > 1:
            self.assign(values, candidates[0], value)

    def solve(self, mother):
        if not mother:
            return False
        if __name__ == "__main__":
            clear()
        if (time.time() - self.start_time) > 120:
            return False

        if solved(mother) == 1:
            return mother
        elif solved(mother) == -1:
            return False

        find = self.find(mother)

        child = copy.deepcopy(mother)
        self.assign(child, find[0], find[1])

        child = self.solve(child)
        if child:
            return child
        else:
            self.remove(mother, find[0], find[1])
            return self.solve(mother)

    def find(self, values):
        for l in self.letters:
            for n in self.numbers:
                if len(values[l + n]) > 1:
                    return l + n, values[l + n][0]


if __name__ == "__main__":
    print("Was main, solving")
    puzzle = "800000000003600000070090200050007000000045700000100030001000068008500010090000400"  # arto
    val = dict()
    let = "ABCDEFGHI"
    num = "123456789"
    for n in range(0, 9):
        for l in range(0, 9):
            val[let[l] + num[n]] = puzzle[n * 9 + l]

    solver = Solver(val)

