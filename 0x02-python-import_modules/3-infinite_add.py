#!/usr/bin/python3
def integer(num):
    """My integer function
    Args:
        num: integer number
    Return:
        Returns integer
    """
    return (int(num))


if __name__ == "__main__":
    from sys import argv

    int_sum = 0

    if len(argv) == 1:
        print("{:d}".format(0))
    elif len(argv) > 1:
        for i in range(1, len(argv)):
            int_sum += integer(int(argv[i]))
        print(int_sum)
