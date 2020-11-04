# Basic String operations

first_message = "This a very long string."
second_message = "I can use a lot of string operations here."
another_string = "xyz-"

# Concatenated strings
concatenated = first_message + " " + second_message
print(concatenated)

# Repeated strings
repeated = first_message * 2
another_string_again = another_string * 3
print(repeated)
print(another_string_again)

# Slicing

slice1 = first_message[2:]  # is a very long string.
slice2 = first_message[:2]  # Th
slice3 = first_message[2:18:2]

print(slice1)
print(slice2)
print(slice3)

# slices_concatenated = slice2 + slice1
# print(slices_concatenated)

slice3 = first_message[2:]
slice4 = first_message[:4]
slice5 = first_message[::2]

# What would the following lines print?
print(slice3)
print(slice4)
print(slice5)
