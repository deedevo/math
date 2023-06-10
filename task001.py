# Trapezoidal Method

# Define function to integrate
# def f(x):
#     return x*x*x
def f(x):
    return 1/x


# Implementing trapezoidal method
def trapezoidal(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h
        integration = integration + 2 * f(k)

    # Finding final integration value
    integration = integration * h / 2

    return integration


# Input section
lower_limit = 1
upper_limit = 3
sub_interval = 1

# Call trapezoidal() method and get result
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (result))
