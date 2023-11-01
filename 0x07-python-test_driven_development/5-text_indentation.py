#!/usr/bin/python3
"""text module"""


def text_indentation(text):
    """text function for alx

    Args:
        text (string): first argument

    Raises:
        TypeError: if first argument is not string
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    for space in ".?:":
        # print(delim, text.split(delim))
        text = (space + "\n\n").join(
            [line.strip(" ") for line in text.split(space)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
