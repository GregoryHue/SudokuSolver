import controller
import sys
import inquirer



def main():

    questions = [
    inquirer.List('difficulty',
                    message="Which difficulty?",
                    choices=['beginner', 'easy', 'medium', 'hard', 'extreme'],
                ),
    ]
    name = inquirer.prompt(questions)

    controller.StartSudokuSolver(name["difficulty"])

    print("Completed.\nCheck 'app/files/" + name["difficulty"] + "-output.txt' to see the result and 'app/files/log.txt' to see every steps in details.")

if __name__ == '__main__':
    main()
