# PySudokuSolver

Python script to solve a Sudoku.

## Project setup

Get into the project folder:
```bash
cd PySudokuSolver
```

Create a new environment:

```bash
virtualenv --python="/usr/local/bin/python3" env
```

Get into that environment:

```bash
source env/bin/activate 
```

Install the librairies:
```bash
pip install -r requirements.txt
```

## Usage

Run:

```bash
python3 app/src/main.py
```

This will display a prompt where you can choose which difficulty of Sudoku you want to solve. The result will be displayed in the console. A log file detailing every step can be found in `app/files/log.txt`.

Note : The difficulties "hard" and "extreme" aren't always completed.

## Versions

* Python 3.8.10
* Ubuntu 20.04.5

## Structure

```
app/
env/
.gitignore
README.md
```

## TODO

* Rework the random steps to make sure hard and extreme are always completed.
* Make it executable with command line
* Add parameters
* Add interface
