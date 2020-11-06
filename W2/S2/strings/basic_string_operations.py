# Basic String operations

first_message = "This a very long string."
second_message = "I can use a lot of string operations here."
another_string = "xyz-"

# > Length of a string

print(f"'first_message' has {len(first_message)} characters.")
print(f"'second_message' has {len(second_message)} characters.")
print(f"'another_string' has {len(another_string)} characters.")


# > Concatenated strings
concatenated = first_message + " " + second_message
print(concatenated)

print(first_message + " " + second_message)

# > Repeated strings
repeated = first_message * 2
another_string_again = another_string * 3
print(repeated)
print(another_string_again)

# > Membership Test

# We can test if a substring exists (True / False) within a string or not, using the keyword in.

print("Is 'xyz' in 'first_message'?", 'xyz' in first_message)
print("Is 'xyz' in 'second_message'?", 'xyz' in second_message)
print("Is 'xyz' in 'another_message'?", 'xyz' in another_string)

# > Slicing [first:last:step]

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# T h i s   a   v e r y     l  o  n  g     s  t  r  i  n  g  .

slice1 = first_message[2:]      # is a very long string.
slice2 = first_message[:2]      # Th
slice3 = first_message[2:18:2]  # i  eyln

print(slice1)
print(slice2)
print(slice3)

slices_concatenated = slice2 + slice1
print(slices_concatenated)

# > WWTP?

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# T h i s   a   v e r y     l  o  n  g     s  t  r  i  n  g  .

slice3 = first_message[2:]
slice4 = first_message[:4]
slice5 = first_message[::2]

print(slice3)   # is a very long string.
print(slice4)   # This
print(slice5)   # Ti  eyln tig


# > Built-in Functions

# >> enumerate()
first_list = list(enumerate(first_message))
second_list = list(enumerate(second_message))

# print(f"List of characters in 'first_message' = {first_list}")
# print(f"List of characters in 'second_message' = {second_list}")

# >> The list() function

my_string = "0123456789"
my_list = list(my_string)
print(my_list[0])
print(my_list[1])
print(my_list[-2])
print(my_list[-1])

print(f"The type is {type(my_list)}.")
print(f"The type is {type(my_list[0])}.")
