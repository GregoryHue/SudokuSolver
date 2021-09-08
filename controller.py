import time


# Working, read a csv file in /files, given its name, and return its content
def ReadFile(name):
    data = []
    with open('files/' + name + '.txt') as file:
        file.seek(0)
        idx_row = 0
        for row in file:
            s_row = row.rstrip().split(' ')
            if s_row:
                data.append([])
                for number in s_row:
                    data[idx_row].append(number)
                idx_row += 1
        return data


# Working, create a csv file in /files, and write the data inside
def WriteFile(name, data):
    with open('files/' + name + '.txt', 'w') as newfile:
        for row in data:
            newfile.writelines(' '.join(row) + '\n')


# Working, return True if a cell is still empty
def SudokuUnfinished(data):
    for row in data:
        if '*' in row:
            return True
    return False


def TryToSolve(data):
    while SudokuUnfinished(data):
        suggestions = CreateSuggestions(data)
        ShowTableAndSuggestion(data, suggestions)
        SingledOutSuggestions(suggestions, data)

        suggestions = CreateSuggestions(data)
        CheckSuggestions(suggestions, data)

        suggestions = CreateSuggestions(data)
        # PairSuggestions(suggestions, data)

    return data


# Working, for every cell that has only 1 suggestion, it confirms it and write it in data
def SingledOutSuggestions(suggestions, data):
    for row in suggestions:
        if len(suggestions[row]) == 1:
            data[row[0]][row[1]] = suggestions[row][0]
    return suggestions


# Working, check for every cell, every possible number, then write it in suggestions = {}
def CreateSuggestions(data):
    suggestions = {}
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
                            suggestions[x, y].append(str(number))
                        except KeyError:
                            suggestions[x, y] = [str(number)]
                y += 1
            x += 1
    return suggestions


def CheckSuggestions(suggestions, data):
    for row in suggestions:
        for suggestion in suggestions[row]:
            if IsOnlySuggestionInLine(suggestions, suggestion, row[0]):
                data[row[0]][row[1]] = suggestion
            if IsOnlySuggestionInColumn(suggestions, suggestion, row[1]):
                data[row[0]][row[1]] = suggestion
            if IsOnlySuggestionInSquare(suggestions, suggestion, row[0], row[1]):
                data[row[0]][row[1]] = suggestion
    return suggestions


def IsOnlySuggestionInLine(suggestions, suggestion, line):
    same_suggestion_found = 0
    for row in suggestions:
        for original_sug in suggestions[row]:
            if row[0] == line and original_sug == suggestion:
                same_suggestion_found += 1

    if same_suggestion_found == 1:
        return True
    return False


def IsOnlySuggestionInColumn(suggestions, suggestion, column):
    same_suggestion_found = 0
    for row in suggestions:
        for original_sug in suggestions[row]:
            if row[1] == column and original_sug == suggestion:
                same_suggestion_found += 1

    if same_suggestion_found == 1:
        return True
    return False


def IsOnlySuggestionInSquare(suggestions, suggestion, line, column):
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

    for row in suggestions:
        for original_sug in suggestions[row]:
            if limits[0] <= row[0] <= limits[1] and limits[2] <= row[1] <= limits[3] and original_sug == suggestion:
                same_suggestion_found += 1

    if same_suggestion_found == 1:
        return True
    return False


# TOFINISH
def PairSuggestions(suggestions, data):
    for row in suggestions:
        idx = 0
        for candidate in suggestions[row]:
            print(row, suggestions[row])
            idx += 1
            for x in range(idx, len(suggestions[row])):
                pairs = candidate, suggestions[row][x]
                print(pairs)


# Working, return True if an array contains a number, used to check line, column, and group
def IsNumberInArray(array, number):
    if str(number) in array:
        return True
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


# TODO : add line for each number added; write in a log file
def ShowTableAndSuggestion(data, suggestions):
    print('Row | Column | Candidates')

    for row in suggestions:
        print(' ', row[0] + 1, '    ', row[1] + 1, '   ', suggestions[row])

    print('\n      Table')

    for row in data:
        print(' '.join(row))
    print('')
