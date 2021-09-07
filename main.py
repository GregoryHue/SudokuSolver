import controller as controller


def main():
    name = 'hard'

    data = controller.ReadFile(name)
    controller.TryToSolve(data)
    controller.WriteFile(name + '-output', data)

    print("Completed ... ?")

if __name__ == '__main__':
    main()
