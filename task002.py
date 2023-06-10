# Simpson's 1/3 Rule
import math
# Define function to integrate
# def f(x):
#     return math.sin(x)
def f(x):
    return math.sqrt(math.cos(x))
def f(x):
    return 1 / 1 + x


# Implementing Simpson's 1/3
def simpson13(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h

        if i % 2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)

    # Finding final integration value
    integration = integration * h / 3

    return integration


# Input section
lower_limit = 0
upper_limit = math.pi
sub_interval = 11

# lower = 0
# upper = math.pi/2
# interval = 9
lower = 0
upper = 1
interval = 5

# Call trapezoidal() method and get result
# first = simpson13(lower_limit, upper_limit, sub_interval)
second = simpson13(lower, upper, interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (second))
