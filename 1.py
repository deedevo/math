import math


def false_position_method(function, a, b):
    if (function(a) * function(b)) >= 0:
        print("No answer")
        return
    c = 0
    iterations = 1000000
    for i in range(iterations):
        function_difference = function(b) - function(a)
        c = (a * function(b) - b * function(a)) / function_difference
        if function(c) * function(a) < 0:
            b = c
            print("Result: ", round(c, 5))
        else:
            a = c
            print("Result: ", round(c, 5))
    print("Result:", round(c, 5))


def f1(x):
    return x * x * x - 5 * x + 1


def f2(x):
    return x * math.exp(x) - 2


def f3(x):
    return math.cos(x) - 3 * x + 1


def f4(x):
    return 2 * x - math.log(x) - 7


def f5(x):
    return pow(x, 10) - 1


a = -10  # b
b = 10  # b
a1 = 1  # b
b1 = 2
false_position_method(f1, -10, 10)
