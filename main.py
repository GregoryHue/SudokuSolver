import controller as controller


def main():
    name = 'extreme'

    data = controller.ReadFile(name)
    controller.TryToSolve(data)
    controller.WriteFile(name + '-output', data)

    print("Completed ... ?")


def main_old():
    controller.GenerateSudoku('new_sudoku')

    print("End of script")


if __name__ == '__main__':
    main()
