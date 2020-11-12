# More about Functions

import math

# > Function Composition

x = math.sin(360*2*math.pi)
print(x)
# Prints -3.133115067780141e-14

x = math.exp(math.log(3.14))
print(x)
# Prints 3.1399999999999997

# > Nested Functions


def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


result = outer(2, 4)

print(result)
# Prints 6
