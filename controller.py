import csv


# Working, read a csv file in /files, given its name, and return its content
def ReadFile(name):
    data = []
    with open('files/' + name + '.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        csvfile.seek(0)
        idx_row = 0
        for row in reader:
            if row:
                data.append([])
                for number in row:
                    data[idx_row].append(number)
                idx_row += 1
        return data


# Working, create a csv file in /files, and write the data inside
def WriteFile(name, data):
    writer = csv.writer(open('files/' + name + '.csv', 'w', newline=''))
    writer.writerows(data)



# Working, return True if a cell is still empty
def SudokuUnfinished(data):
    for row in data:
        if '*' in row:
            return True
    return False


def TryToSolve(data):
    suggestions = {}
    CreateSuggestions(suggestions, data)
    ExecuteSuggestions(suggestions, data)
    for row in suggestions:
        print(row, suggestions[row])
    return data


# Working, for every cell that has only 1 suggestion, it confirms it and write it in data
def ExecuteSuggestions(suggestions, data):
    for row in suggestions:
        if len(suggestions[row]) == 1:
            data[row[0]][row[1]] = suggestions[row][0]
    return suggestions


# Working, check for every cell, every possible number, then write it in suggestions = {}
def CreateSuggestions(suggestions, data):
    for number in range(1, 10):
        x = 0
        for row in data:
            y = 0
            for cell in row:
                if cell == '*':
                    if not IsNumberInArray(Line(data, x), number) and not IsNumberInArray(Column(data, y), number) and not IsNumberInArray(
                            Group(data, x, y), number):
                        try:
                            suggestions[x, y].append(str(number))
                        except KeyError:
                            suggestions[x, y] = [str(number)]
                y += 1
            x += 1
    return suggestions

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
