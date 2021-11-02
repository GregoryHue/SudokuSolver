# PySudoSolver

Python script to solve a Sudoku.

This script solves Sudokus, between 5 difficulties (beginner, easy, medium, hard, extreme).

As of today, it uses 3 different methods to complete the Sudoku :

* Single cell : write down a number if it's the only possibility in that cell.

* Single line / column / square : write down a number if it's the only possibility in a line, column or square.

* Random step : when it finds nothing to write down, it creates a back-up of the current state of the Sudoku and try a random step, amongs the possibilities. In case this leads to a failure, it comes back to that back-up.

After every step, a function to generate the possibilities is called.

# TODO

Add a generator of Sudoku.

Add a step by step explanation.