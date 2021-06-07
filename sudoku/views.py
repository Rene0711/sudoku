from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import sudoku.generator
import sudoku.new_solver

from django.shortcuts import render, redirect
from sudoku.solver import Solver
from sudoku.new_solver import solver
from sudoku.trainer import trainer


def index(request):
    return render(request, 'sudoku/home.html')


@csrf_exempt
def sudoku_solver(request):
    if request.POST:
        if request.POST['gen'] == "1":
            values = sudoku.generator.get_grid(False)
            return render(request, 'sudoku/solver.html', {'values': values})
        if request.POST['gen'] == '2':
            values = sudoku.generator.get_grid(True)
            return render(request, 'sudoku/solver.html', {'values': values})
        else:
            values = dict()
            candidates = dict()

            for l in "ABCDEFGHI":
                for n in "123456789":
                    try:
                        values[l + n] = request.POST[l + n]
                    except:
                        pass

                    for c in "123456789":
                        try:
                            candidates[l + n + "-" + c] = request.POST[l + n + "-" + c]
                        except:
                            pass

            values, hints, candidates = sudoku.new_solver.solver(values, candidates)
            return render(request, 'sudoku/solver.html', {'values': values,
                                                          'hints': hints,
                                                          'candidates': candidates})
    else:
        return render(request, 'sudoku/solver.html')


def sudoku_creator(request):
    return render(request, 'sudoku/creator.html')


def sudoku_trainer(request):
    return render(request, 'sudoku/trainer.html')


def strategies(request):
    if request.POST:
        values = dict()
        candidates = dict()

        for l in "ABCDEFGHI":
            for n in "123456789":
                try:
                    values[l + n] = request.POST[l + n]
                except:
                    pass

                for c in "123456789":
                    try:
                        candidates[l + n + "-" + c] = request.POST[l + n + "-" + c]
                    except:
                        pass
        values, hints, candidates = trainer(values, candidates)
        return render(request, 'sudoku/strategies.html', {'values': values})
    else:
        return render(request, 'sudoku/strategies.html')
