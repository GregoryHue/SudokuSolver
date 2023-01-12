import controller
import sys


def main():

    name = 'extreme'
    orig_stdout = sys.stdout
    f = open('app/files/log.txt', 'w')
    sys.stdout = f

    controller.StartSudokuSolver(name)

    sys.stdout = orig_stdout
    f.close()
    print("Completed.\nCheck 'app/files/" + name + "-output.txt' to see the result and 'app/files/log.txt' to see every steps in details.")

if __name__ == '__main__':
    main()
