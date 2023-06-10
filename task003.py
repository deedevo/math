# Simpson's 3/8 Rule
import math
# Define function to integrate
# def f(x):
#     return 1 / (1 + x*x*x)

def f(x):
    return math.sin(x)

# Implementing Simpson's 3/8
def simpson38(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h

        if i % 3 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)

    # Finding final integration value
    integration = integration * 3 * h / 8

    return integration


# Input section
lower_limit = 0
upper_limit = 9
sub_interval = 3

lower = 0
upper = math.pi/2
interval = 9

# Call trapezoidal() method and get result
# first = simpson38(lower_limit, upper_limit, sub_interval)
second = simpson38(lower, upper, interval)
print("Integration result by Simpson's 3/8 method is: %0.6f" % (second))