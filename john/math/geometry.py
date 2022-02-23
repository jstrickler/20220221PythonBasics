"""
Math utilities

These are some random math utilities.

Enjoy them.
"""
from math import pi

ANIMAL = "wombat"

def circle_area(diameter):
    """
    Compute the area of a circle, given its diameter.

    :param diameter: Diameter of the circle
    :return: area of circle
    """
    radius = diameter / 2
    return pi * (radius ** 2)


def rectangle_area(length, width):
    """
    Computer the area of a rectangle, given length and width

    :param length: Length of longest dimension
    :param width: Length of shortest dimension
    :return: Area of rectangle
    """
    return length * width


def square_area(length):
    """
    Compute area of a square, given length of one side.

    :param length: Length of one side.
    :return: area of the square
    """
    return length ** 2


# "private"
def _doit():
    pass

