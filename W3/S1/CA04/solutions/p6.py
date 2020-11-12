""" 6. Given a string, get the length of the string without using the `len()` function.
"""

my_string = "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering."

length = 0

for c in my_string:
    length += 1

print(f"The length of my string is {length}.")
