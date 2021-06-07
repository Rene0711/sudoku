from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sudoku-trainer', views.sudoku_trainer, name='sudoku-trainer'),
    url(r'^strategies', views.strategies, name='strategies'),
    url(r'^sudoku-solver', views.sudoku_solver, name='sudoku-solver'),
    url(r'^sudoku-creator', views.sudoku_creator, name='sudoku-creator'),
    url(r'^', views.index, name='index'),
]
