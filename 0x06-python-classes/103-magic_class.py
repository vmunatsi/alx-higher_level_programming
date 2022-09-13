#!/usr/bin/python3
import math


class MagicClass:
    """Square.
    Attributes:
        size (int): size of the side of the square.
        position (tuple): Position of the square printed.
    """
    def __init__(self, radius):
        """ __init__ """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            pass
        self.__radius = radius

    def area(self):
        """ area """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """circumference """
        return (2 * math.pi * self.__radius)
