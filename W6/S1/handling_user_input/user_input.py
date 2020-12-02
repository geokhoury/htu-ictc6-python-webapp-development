# IO Basics

# The difference between input() and raw_input()
# ** The raw_input() function was built in Python 2. It is deprecated in version 3.


# > Using the input() function
number = input("Please enter a number: ")
print(f"You entered: {number}.")

# > Using the input() function and parsing into a list
number_list = list(input("Please enter a number: "))
print(f"You entered: {number_list}.")

# > Using the input() function and parsing into a tuple
number_tuple = tuple(input("Please enter a number: "))
print(f"You entered: {number_tuple}.")