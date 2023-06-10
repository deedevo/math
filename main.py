import math


def bisection(function, a, b):
    if (function(a) * function(b)) >= 0:
        print("No answer")
        return
    c = 0
    while (b - a) >= 0.001:
        c = (a + b) / 2
        if function(c) * function(a) < 0:
            b = c
            print("Result: ", round(c, 5))
        else:
            a = c
            print("Result: ", round(c, 5))

    print("Result: ", round(c, 3))


def f1(x):
    return x * x * x - 4*x + 9


def f2(x):
    return x - math.cos(x)


def f3(x):
    return math.exp(-x) - x


def f4(x):
    return pow(x, 10) - 1  # c


a = -3  # a
b = -2  # a
a1 = 0
b1 = 10
bisection(f1, a, b)
