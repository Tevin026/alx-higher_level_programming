#!/usr/bin/python3
'''
    printing square
'''


def print_square(size):
    '''
        a function that prints a square with the character #.

        Arg: size

        Raises:
            TypeError: if size is not an Integer

    '''

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
