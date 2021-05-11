import sudoku.generator
import sudoku.new_solver

from django.shortcuts import render, redirect
from sudoku.solver import Solver
from sudoku.new_solver import solver


def index(request):
    if request.GET:
        if request.GET['gen'] == '1':
            values = sudoku.generator.get_grid(False)
            return render(request, 'sudoku/index.html', {'values': values})
        if request.GET['gen'] == '2':
            values = sudoku.generator.get_grid(True)
            return render(request, 'sudoku/index.html', {'values': values})
        else:
            valid = True
            values = dict()
            setup = False
            for l in "ABCDEFGHI":
                for n in "123456789":
                    if l + n not in request.GET:
                        valid = False
                    else:
                        if len(request.GET[l + n]) > 1:
                            valid = False
                        elif len(request.GET[l + n]) == 1:
                            if request.GET[l + n] not in "123456789":
                                valid = False
                            else:
                                values[l + n] = request.GET[l + n]
            if valid:
                values = sudoku.new_solver.solver(values)
                #values = Solver(values).values
                if values:
                    return render(request, 'sudoku/index.html', {'values': values})
            return redirect('index')
    else:
        return render(request, 'sudoku/index.html')


def generate(request):
    return True
