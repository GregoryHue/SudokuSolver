import controller as controller
import time


def main():
    name = 'testing'

    data = controller.ReadFile(name)
    while controller.SudokuUnfinished(data):
        data = controller.TryToSolve(data)

        for row in data:
            print(' '.join(row))
        controller.WriteFile(name + '-output', data)
        time.sleep(0.5)
        print('\n'*3)
    print("Completed ... ?")

if __name__ == '__main__':
    main()
