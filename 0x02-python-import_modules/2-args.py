#!/usr/bin/python3
def print_str(str):
    """Print string function
    Args:
        str: string to be printed
    Returns:
        The string to be printed
    """
    print("{}".format(str))


if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("{:d}: ".format(1), end="")
        print_str(str(argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: ".format(i), end="")
            print_str(str(argv[i]))
