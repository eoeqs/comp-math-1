from getter import *
from solver import *


def main():
    accuracy = float(get_accuracy())
    dimension = int(get_dimension())
    matrix = get_matrix(dimension)
    print_matrix(matrix)
    # accuracy = float(accuracy)
    # dimension = int(dimension)
    iterate_matrix(matrix, accuracy, dimension)


main()
