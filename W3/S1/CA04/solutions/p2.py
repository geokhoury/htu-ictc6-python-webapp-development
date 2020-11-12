""" 2. Write a program which prints the following pattern for any given number, `n = 5`, for example.
* 1
* 1 2
* 1 2 3
* 1 2 3 4
* 1 2 3 4 5
"""

# Ask user for integer input
n = int(input("Please enter a number: "))

# Define an empty string
my_string = ""

# Iterate over the range 1, n+1
for i in range(1, n+1):
    # Concatenate the string
    my_string += str(i) + " "
    print(my_string)
