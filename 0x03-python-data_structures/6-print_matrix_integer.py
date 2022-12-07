#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
	    print("{:d} {:d}".format(i, j, end=""))
