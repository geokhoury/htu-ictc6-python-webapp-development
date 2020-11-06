# String Methods

# > Accessing string characters in Python

some_string = "Hello, world!"
another_string = "Hello again!"

# > Get the length of the strings
string_length = len(some_string)    # this is a function call
another_length = len(another_string)

# > Print the length
print("The length of the string '%s' is %d." % (some_string, string_length))
print("The length of the string '%s' is %d." %
      (another_string, another_length))

print("The length of the string '%s' is: %d" % (some_string, len(some_string)))

# > Case methods, upper(), lower(), and capitalize()

print("This is the uppercase version of 'some_string': %s" % some_string.upper())
print("This is the lowercase version of 'some_string': %s" % some_string.lower())
print("This is the capitalized version of 'some_string': %s" % some_string.capitalize())

# > Count

print(another_string.count('a'))          # 2
print(another_string.count('l'))          # 2
print(another_string.count('H'))          # 1
print(another_string.count('Hello'))      # 1

# > Find the index of a character

print(
    f"The index of the first 'o' in 'some_string' is: {some_string.index('o')}")

# > Substrings (slicing)
print("A substring between 3 and 7 from 'some_string' is: %s" %
      some_string[3:7])

print("A substring between 2 and 8 with steps of 2 from 'some_string' is: %s" %
      some_string[2:8:2])

# > Split

my_new_string = "Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
my_string_list = my_new_string.split(',')

print(my_string_list)

my_new_string = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday"
my_string_list = my_new_string.split()    # split based on space

print(my_string_list)
