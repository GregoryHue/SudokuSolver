import view as view
import controller as controller
import csv


def main():
    data = []
    with open('files/' + 'easy' + '.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        view.ShowTable(reader)
        csvfile.seek(0)
        for row in reader:
            data.append(row)

        controller.TryToSolve(data)


if __name__ == '__main__':
    main()
