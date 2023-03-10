from math import sqrt

a = 7
b = 2
c = 8


def triangle_perimetr(s_a=a, s_b=b, s_c=c):
    return s_a + s_b + s_c


def triangle_area(s_a=a, s_b=b, s_c=c):
    p = (s_a + s_b + s_c) / 2
    return sqrt(p * (p - s_a) * (p - s_b) * (p - s_c))
