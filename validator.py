import os


def validate_choice(choice):
    if choice in ["1", "2", "3"]:
        return True
    else:
        return False


def validate_filename(name):
    if os.path.isfile(name):
        return True
    else:
        return False


def validate_accuracy(accuracy):
    try:
        if float(accuracy) > 0:
            return True
        return False
    except ValueError:
        return False


def validate_dimension(dimension):
    try:
        if 2 <= int(dimension) <= 20:
            return True
        return False
    except ValueError:
        return False


def validate_matrix(row, size):
    if len(row) != size + 1:
        print("Wrong number of coefficients.")
        return False
    for i in row:
        try:
            float(i)
        except ValueError:
            print("Matrix should contain only numbers.")
            return False
    return True
