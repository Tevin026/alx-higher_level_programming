#!/usr/bin/python3
'''
    Printing text
'''


def text_indentation(text):
    '''
        a function that prints a text with 2 new lines


        Arg: text

        Raises:
            TypeError: if text is not a string
    '''

    if type(text) != str:
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join([s.strip(" ") for s in text.split(char)])
    print(text, end="")
