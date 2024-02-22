from validator import *
import random


def get_accuracy_from_user():
    print("Input accuracy: ")
    accuracy = get_value()
    while not validate_accuracy(accuracy):
        print("Please enter valid accuracy: ")
        accuracy = get_value()
    return accuracy


def get_accuracy_from_file(filename):
    with open(filename, "r") as file:
        first_line = file.readline().strip()
        try:
            accuracy = float(first_line)
            if len(first_line.split()) > 1:
                raise ValueError("Accuracy should be a single number in the first line of the file.")
            return accuracy
        except ValueError:
            print("Error: Invalid format in the first line of the file. Accuracy should be a single number.")
            return None


def get_accuracy(choice):
    accuracy = 1

    match choice:
        case "1":
            accuracy = get_accuracy_from_user()
            while not validate_accuracy(accuracy):
                print("Accuracy from input is not valid.")
                accuracy = get_value()
        case "2":
            while True:
                filename = get_filename()
                accuracy = get_accuracy_from_file(filename)
                if not validate_accuracy(accuracy):
                    print("Accuracy from file is not valid.")
                    continue
                break
        case "3":
            accuracy = get_accuracy_from_user()
            while not validate_accuracy(accuracy):
                print("Accuracy for random matrix is not valid.")
                accuracy = get_value()
        case _:
            print("Please enter a valid choice (1, 2 or 3). ")
    return accuracy


def get_dimension(choice):
    dimension = 1
    match choice:
        case "1":
            print("Input dimension [2, 20]: ")
            dimension = get_value()
            while not validate_dimension(dimension):
                print("Dimension from input is not valid.")
                dimension = get_value()
        case "2":
            while True:
                filename = get_filename()
                dimension = get_dimension_from_file(filename)
                if not validate_dimension(dimension):
                    print("Dimension from file is not valid.")
                    continue
                break
        case "3":
            print("Input dimension [2, 20]: ")
            dimension = get_value()
            while not validate_dimension(dimension):
                print("Dimension for random matrix is not valid.")
                dimension = get_value()
        case _:
            print("Please enter a valid choice (1, 2 or 3). ")
    return dimension


def get_dimension_from_file(filename):
    with open(filename, "r") as file:
        second_line = file.readlines()[1]
        try:
            dimension = int(second_line)
            if len(second_line.split()) > 1:
                raise ValueError("Dimension should be a single integer in the second line of the file.")
            return dimension
        except ValueError:
            print("Error: Invalid format in the second line of the file. Dimension should be a single integer.")
            return None


def get_value():
    value = input().strip()
    value = value.replace(',', '.')
    return value


def get_filename(filename=None):
    if filename:
        return filename
    print("Input file name: ")
    filename = get_value()
    while not validate_filename(filename):
        print("Input correct file name: ")
        filename = get_value()
    return filename


def get_matrix(choice, dimension, filename=None):
    dimension = int(dimension)
    matrix = []
    choice = str(choice)

    match choice:
        case "1":
            matrix = get_matrix_from_input(dimension)
        case "2":
            # filename = get_filename()
            matrix = get_matrix_from_file(filename, dimension)
        case "3":
            matrix = get_random_matrix(dimension)
    return matrix


def get_random_matrix(dimension):
    matrix = [[0] * (dimension + 1) for _ in range(dimension)]
    for i in range(dimension):
        for j in range(dimension + 1):
            matrix[i][j] = random.randint(-9, 9)
    return matrix


def get_matrix_from_input(dimension):
    matrix = []
    dimension = int(dimension)
    print("Enter the coefficients of the matrix by rows ({} coefficients in each row): ".format(str(dimension + 1)))
    for i in range(dimension):
        try:
            row = [i for i in input().split()]
            while not validate_matrix(row, dimension):
                row = [i for i in input().split()]
            row = [float(i) for i in row]
            matrix.append(row)
        except ValueError:
            print("Matrix should contain numbers only.")
    return matrix


def get_matrix_from_file(filename, dimension):
    matrix = []
    with open(filename, "r") as file:
        lines = file.readlines()[2:]
        if len(lines) <= 1:
            print("File is empty.")
        for i in range(len(lines)):
            try:
                row = [float(i) for i in lines[i].split()]
                if validate_matrix(row, dimension):
                    matrix.append(row)
                else:
                    matrix = []
                    break
            except ValueError:
                print("Matrix should contain numbers only.")
    return matrix


def get_one_string_from_file(filename):
    with open(filename, "r") as file:
        a = file.readline()
        return a


def get_choice(choice=None):
    if choice is None:
        choice = input().strip()
    while not validate_choice(choice):
        print("Invalid choice. Please enter a valid choice: ")
        choice = input().strip()

    return choice
