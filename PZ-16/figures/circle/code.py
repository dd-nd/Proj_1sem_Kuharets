from math import pi

default_radius = 5


def circle_perimetr(s_radius = default_radius):
    return pi * 2 * s_radius


def circle_area(s_radius = default_radius):
    return pi * s_radius ** 2