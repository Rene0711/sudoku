from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import sudoku.generator
import sudoku.new_solver

from django.shortcuts import render, redirect
from sudoku.solver import Solver
from sudoku.new_solver import solver


def index(request):
    return render(request, 'sudoku/home.html')


@csrf_exempt
def sudoku_solver(request):
    print(request.POST)
    if request.POST:
        if request.POST['gen'] == "1":
            values = sudoku.generator.get_grid(False)
            return render(request, 'sudoku/solver.html', {'values': values})
        if request.POST['gen'] == '2':
            values = sudoku.generator.get_grid(True)
            return render(request, 'sudoku/solver.html', {'values': values})
        else:
            valid = True
            values = dict()
            setup = False
            for l in "ABCDEFGHI":
                for n in "123456789":
                    if l + n not in request.POST:
                        valid = False
                    else:
                        if len(request.POST[l + n]) > 1:
                            valid = False
                        elif len(request.POST[l + n]) == 1:
                            if request.POST[l + n] not in "123456789":
                                valid = False
                            else:
                                values[l + n] = request.POST[l + n]
            if valid:
                values, hints, candidates = sudoku.new_solver.solver(values)
                if values:
                    return render(request, 'sudoku/solver.html', {'values': values,
                                                                  'hints': hints,
                                                                  'candidates': candidates})
            return redirect('index')
    else:
        print(request)
        return render(request, 'sudoku/solver.html')


def sudoku_creator(request):
    return render(request, 'sudoku/creator.html')


def sudoku_trainer(request):
    return render(request, 'sudoku/trainer.html')
