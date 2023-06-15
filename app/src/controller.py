import random
import view
import model
import sys

# Example :
# possibility : {(1, 0): ['1', '2', '4', '7', '9'], (1, 1): ['1', '4', '7', '9'], (1, 2): ['1', '2', '9'] ... }
# data : [['3', '6', '8', '1', '2', '4', '7', '9', '5'], ['*', '*', '*', '*', '3', '*', '*', '*', '6'] ... ]


# Working, return True if a cell is still empty
def SudokuUnfinished(data):
    for row in data:
        if '*' in row:
            return True
    return False


def StartSudokuSolver(name):
    data = model.ReadFile(name)
    # Showing the original file
    print('    Original')
    with open('app/files/' + name + '.txt', 'r') as o:
        print(o.read())
        
    # Redirecting prints into a log file
    orig_stdout = sys.stdout
    f = open('app/files/log.txt', 'w')
    sys.stdout = f

    # Solving the Sudoku
    TryToSolve(data)
    model.WriteFile(name + '-output', data)

    # Redirecting prints back to the console
    sys.stdout = orig_stdout
    f.close()

    # Showing the result file
    print('\n     Result')
    with open('app/files/' + name + '-output.txt', 'r') as r:
        print(r.read())


def TryToSolve(data):
    safe_data = []

    while SudokuUnfinished(data):

        old_data = []
        for row in data:
            old_data.append(row.copy())

        possibilities = CreateSuggestions(data)
        SingledOutSuggestions(possibilities, data)

        possibilities = CreateSuggestions(data)
        CheckSuggestions(possibilities, data)

        if SameLists(data, old_data):
            if not safe_data:
                for row in data:
                    safe_data.append(row.copy())
                print("Creating a safe data")
            elif not possibilities:
                data = []
                for row in safe_data:
                    data.append(row.copy())
                print("Returning to safe data")

            possibilities = CreateSuggestions(data)
            TryRandomSuggestion(data, possibilities)

    return data


# Working, for every cell that has only 1 possibility, it confirms it and write it in data
def SingledOutSuggestions(possibilities, data):
    for row in possibilities:
        if len(possibilities[row]) == 1:
            view.NextStep()
            data[row[0]][row[1]] = possibilities[row][0]
            view.ShowStep(possibilities[row][0], row[0] + 1, row[1] + 1, "Only possibility in single cell")
            view.ShowTable(data, row[0], row[1])
            return possibilities


# Working, check for every cell, every possible number, then write it in possibilities = {}
def CreateSuggestions(data):
    possibilities = {}
    for number in range(1, 10):
        x = 0
        for row in data:
            y = 0
            for cell in row:
                if cell == '*':
                    if not IsNumberInArray(Line(data, x), number) and not IsNumberInArray(Column(data, y),
                                                                                          number) and not IsNumberInArray(
                        Group(data, x, y), number):
                        try:
                            possibilities[x, y].append(str(number))
                        except KeyError:
                            possibilities[x, y] = [str(number)]
                y += 1
            x += 1
    view.ShowSuggestions(possibilities)
    return possibilities


# Working, write down single possibilities in line, column, and square
def CheckSuggestions(possibilities, data):
    for row in possibilities:
        for possibility in possibilities[row]:
            if IsOnlySuggestionInLine(possibilities, possibility, row[0]):
                view.NextStep()
                data[row[0]][row[1]] = possibility
                view.ShowStep(possibilities[row][0], row[0] + 1, row[1] + 1, "Only possibility in line")
                view.ShowTable(data, row[0], row[1])
                return possibilities
            if IsOnlySuggestionInColumn(possibilities, possibility, row[1]):
                view.NextStep()
                data[row[0]][row[1]] = possibility
                view.ShowStep(possibilities[row][0], row[0] + 1, row[1] + 1, "Only possibility in column")
                view.ShowTable(data, row[0], row[1])
                return possibilities
            if IsOnlySuggestionInSquare(possibilities, possibility, row[0], row[1]):
                view.NextStep()
                data[row[0]][row[1]] = possibility
                view.ShowStep(possibilities[row][0], row[0] + 1, row[1] + 1, "Only possibility in square")
                view.ShowTable(data, row[0], row[1])
                return possibilities


# Working, check if single possibilities in line
def IsOnlySuggestionInLine(possibilities, possibility, line):
    same_suggestion_found = 0
    for row in possibilities:
        for original_sug in possibilities[row]:
            if row[0] == line and original_sug == possibility:
                same_suggestion_found += 1

    if same_suggestion_found == 1:
        return True
    return False


# Working, check if single possibilities in column
def IsOnlySuggestionInColumn(possibilities, possibility, column):
    same_suggestion_found = 0
    for row in possibilities:
        for original_sug in possibilities[row]:
            if row[1] == column and original_sug == possibility:
                same_suggestion_found += 1

    if same_suggestion_found == 1:
        return True
    return False


# Working, check if single possibilities in square
def IsOnlySuggestionInSquare(possibilities, possibility, line, column):
    same_suggestion_found = 0
    limits = []

    x_line = 0
    y_line = 2
    while not limits:
        if x_line <= line <= y_line:
            x_col = 0
            y_col = 2
            while not limits:
                if x_col <= column <= y_col:
                    limits = [x_line, y_line, x_col, y_col]
                x_col += 3
                y_col += 3
        x_line += 3
        y_line += 3

    for row in possibilities:
        for original_sug in possibilities[row]:
            if limits[0] <= row[0] <= limits[1] and limits[2] <= row[1] <= limits[3] and original_sug == possibility:
                same_suggestion_found += 1

    if same_suggestion_found == 1:
        return True
    return False


# Working, return True if an array contains a number, used to check line, column, and group
def IsNumberInArray(array, number):
    if number is None:
        return False

    if not array:
        return False

    if str(number) in array:
        return True
    return False


# Working, return True if an array contains a number, only once, used to check line, column, and group
def IsOnceInArray(array, number):
    count = 0

    if number is None:
        return False

    if not array:
        return False

    for cell in array:
        if str(number) == cell:
            count += 1
    if count == 1:
        return True
    else:
        return False


# Working, return an array corresponding to a line, given a number
def Line(data, line):
    column_content = []
    idx_line = 0
    for row in data:
        if idx_line == line:
            return row
        idx_line += 1


# Working, return an array corresponding to a column, given a number
def Column(data, column):
    column_content = []
    for row in data:
        idx_col = 0
        for cell in row:
            if idx_col == column:
                column_content.append(str(cell))
            idx_col += 1
    return column_content


# Working, return an array corresponding to a group, given a number
def Group(data, line, column):
    group_content = []
    limits = []
    x_line = 0
    y_line = 2

    while not limits:
        if x_line <= line <= y_line:
            x_col = 0
            y_col = 2
            while not limits:
                if x_col <= column <= y_col:
                    limits = [x_line, y_line, x_col, y_col]
                x_col += 3
                y_col += 3
        x_line += 3
        y_line += 3

    x = 0
    for row in data:
        y = 0
        for cell in row:
            if limits[0] <= x <= limits[1] and limits[2] <= y <= limits[3]:
                group_content.append(cell)
            y += 1
        x += 1
    return group_content


# Try a random possibility
def TryRandomSuggestion(data, possibilities):
    random_suggestion = random.randint(0, len(possibilities.keys()))

    i = 0
    for row in possibilities:
        if i == random_suggestion:
            random_number = random.choice(possibilities[row])

            view.NextStep()
            data[row[0]][row[1]] = random_number
            view.ShowStep(random_number, row[0] + 1, row[1] + 1, "Trying a random step")
            return data

        i += 1


# Working, check if two lists are alike
def SameLists(data, old_data):
    x = 0
    for row in data:
        y = 0
        for cell in row:
            if old_data[x][y] != cell:
                return False
            y += 1
        x += 1
    return True


# NOT DONE
def GenerateSudoku(name):
    sudoku_generated = False

    data = []

    while not sudoku_generated:

        row = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        random.shuffle(row)
        data.append(row)
        if not CheckValidity(data):
            del data[-1]

        view.ShowTable(data, row[0], row[1])

        if len(data) == 9:
            sudoku_generated = True

    view.ShowTable(data, row[0], row[1])
    pass


def CheckValidity(data):
    x = 0
    for row in data:
        y = 0
        for cell in row:
            if not IsOnceInArray(Line(data, x), cell) or not IsOnceInArray(Column(data, y), cell) or not IsOnceInArray(
                    Group(data, x, y), cell):
                return False
            y += 1
        x += 1

    return True
