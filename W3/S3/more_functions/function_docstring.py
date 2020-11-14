# Docstring for Functions

""" You can attach documentation to a function definition by including a string literal just after the function header. 
Docstrings are usually triple quoted to allow for multi-line descriptions. """

def hello():
    """This function prints message on the screen.
    This is a new line.
    """

    print('Hello, World!')


# To print a function’s docstring, use the Python help() function and pass the function’s name.

# help(hello)

# You can also access the docstring through __doc__ attribute of the function.

# print(hello.__doc__)

def add(a,b):
    """
        Returns the sum of two integer numbers.

        Parameters:
            a (int): The first operand
            b (int): The second operand

        Returns:
            sum (int): The summation of the values
    """

    return a + b

help(add)
# print(add.__doc__)