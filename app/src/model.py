# Working, read a csv file in /files, given its name, and return its content
def ReadFile(name):
    data = []
    with open('app/files/' + name + '.txt') as file:
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
    with open('app/files/' + name + '.txt', 'w') as newfile:
        for row in data:
            newfile.writelines(' '.join(row) + '\n')


def ReadLog(name):
    data = []
    with open('app/files/' + name + '.txt', 'w') as file:
        file.write("---------- LOG FILE ----------")
        return file
