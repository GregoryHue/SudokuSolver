

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def ShowTable(data):
    colour_line = Bcolors.OKBLUE
    colour_column = Bcolors.OKBLUE
    colour_empty_cell = Bcolors.FAIL

    print(colour_line + ' - - - - - - - - - - - - - - - - - - -' + Bcolors.ENDC)
    idx_row = 0
    for row in data:
        idx_cell = 0
        idx_row += 1
        colour_line = Bcolors.OKBLUE
        if idx_row in [3, 6]:
            colour_line = Bcolors.HEADER
        for cell in row:
            idx_cell += 1
            colour_column = Bcolors.OKBLUE
            if idx_cell in [4, 7]:
                colour_column = Bcolors.HEADER
            if cell == '*':
                print(colour_column + ' | ' + colour_empty_cell + cell + Bcolors.ENDC, end='')
            else:
                print(colour_column + ' | ' + Bcolors.ENDC + cell, end='')
        print(colour_column + ' | ' + Bcolors.ENDC)
        print(colour_line + ' - - - - - - - - - - - - - - - - - - -' + Bcolors.ENDC)
