def SudokuUnfinished(data):
    for row in data:
        if '*' in row:
            return True
    return False


def TryToSolve(data):
    columns = CreateColumns(data)
    groups = CreateGroups(data)
    possible_input = []
    for input in range(1, 9):
        idx_row = -1
        for row in data:
            idx_row += 1
            idx_col = -1
            for cell in row:
                idx_col += 1
                if CheckSameGroup(cell, (idx_row, idx_col)):
                    possible_input.append(input)


def CheckSameLine(cell, row):
    pass


def CheckSameColumn(cell, column):
    pass


def CheckSameGroup(cell, position):
    pass

def CreateColumns(data):
    column = []
    for row in data:
        idx_column = 0
        for cell in row:
            try:
                if column[idx_column] == '':
                    pass
            except IndexError:
                column.append([])
            column[idx_column].append(cell)
            idx_column += 1
    return column

def CreateGroups(data):
    group = []
    new_group = []
    i = 0
    j = 0
    for x in range(i, j):
        pass
