# Strings

# > Accessing string characters in Python

my_string = 'Hello, world!'
print('my_string = ', my_string)

# first character (indexing)
print('my_string[0] = ', my_string[0])

# last character (indexing)
print('my_string[-1] = ', my_string[-1])

# slice from 2nd to the 5th character (slicing)
print('my_string[1:5] = ', my_string[1:5])

# slice from 6th to the 2nd character ()
print('my_string[5:-2] = ', my_string[5:-2])

# # > WWTP?

# print('my_string[15]', my_string[15])     # Will result in IndexError
print('my_string[-1:4]', my_string[-1:4])   # Will return nothing
print('my_string[0]', my_string[0])         # H

# # > Accessing string characters in Python

# my_string[5] = 'a'
# my_string = "Python"
# print(my_string)


# > deleting strings

# del my_string[5]  # This will not work

print(f"Now deleting 'my_string' with the value '{my_string}'.")
del my_string
print(f"Now deleting 'my_string' with the value '{my_string}'.")
