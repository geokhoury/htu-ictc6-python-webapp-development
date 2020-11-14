# Assigning Functions to Variables

# Define a function
def hello():
    print('Hello, World!')

# Assign the function to a variable
hi = hello

# Execute the function
hi()
# Prints Hello, World!

# > WWTP?
print(hello)
print(hi)


# You can use this feature to implement jump table. Jump table is a dictionary of functions to be called on demand.

# Define some functions

def findSquare(x):
    return x ** 2

def findCube(x):
    return x ** 3

# Create a dictionary of functions
exponent = {'square': findSquare, 'cube': findCube}

print(exponent['square'](3))
# Prints 9

print(exponent['cube'](3))
# Prints 27

# > WWTP?
print(exponent['square'])
print(exponent['cube'])