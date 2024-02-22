from getter import *
from solver import *


def main():
    try:
        print("Choose how to input: 1 - from keyboard, 2 - from file, 3 - random numbers")
        choice = get_choice()
        filename = None
        if choice == "1" or choice == "3":
            accuracy = float(get_accuracy(choice))
            dimension = int(get_dimension(choice))
        else:
            filename = get_filename()
            accuracy = float(get_accuracy_from_file(filename))
            dimension = int(get_dimension_from_file(filename))
        matrix = get_matrix(choice, dimension, filename)
        print_matrix(matrix)
        iterate_matrix(matrix, accuracy, dimension)
    except EOFError:
        print("\nEnd of stream detected. Exiting..")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting...")


if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except KeyboardInterrupt:
            print("\nPress Ctrl+C again to exit.")
