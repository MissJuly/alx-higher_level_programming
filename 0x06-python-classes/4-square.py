#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initalizing square.
        Args:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Access private instance attribute 'size'."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set or update private instance attribute 'size'.

        Args:
            value: New value to update 'size'
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the current square area

        Returns:
            Current square area
        """
        return (self.__size * self.__size)
