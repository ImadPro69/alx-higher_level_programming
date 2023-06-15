#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            # Square the value and append it to the new row
            new_row.append(num ** 2)
        # Append the new row to the new matrix
        new_matrix.append(new_row)
    return new_matrix
