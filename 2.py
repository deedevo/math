import math


def secant_method(function, a, b):
    if (function(a) * function(b)) >= 0:
        print("No answer")
        return
    c = 0
    while (b - a) >= 0.001:
        functionDifference = function(a) - function(b)
        c = b - ((a - b) / functionDifference) * function(b)
        if function(c) * function(a) < 0:
            b = c
            print("Result: ", round(c, 5))
        else:
            a = с
            print("Result: ", round(c, 5))
    print("Result:", round(c, 3))


def f(x):
    return x - math.exp(-x)


def f1(x):
    return x * x * x + x * x + x + 7


a = 0
b = 1
a1 = -3
b1 = 3
secant_method(f, a, b)



