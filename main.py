import controller as controller
import time


def main():
    data = controller.ReadFile('extreme')
    while controller.SudokuUnfinished(data):
        data = controller.TryToSolve(data)

        for row in data:
            print('  '.join(row))
        controller.WriteFile('extreme-output', data)
        time.sleep(0.5)
        print('\n'*3)
    print("Completed ... ?")

if __name__ == '__main__':
    main()
