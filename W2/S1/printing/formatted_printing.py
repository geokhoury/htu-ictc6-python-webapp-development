# Older formatting in Python

x = 3
answer_to_life = 42.0
is_whole_number = True
my_name = "Slim Shady"


# printing
print("My name is %s." % my_name)       # string literal
print("My special number is %d." % x)   # int literal
print("The answer to life, the universe and everything is: %0.2f." %
      answer_to_life)   # float literal
print("Some boolean value: %s." % is_whole_number)  # bool literal

# printing more than one
print("My three special numbers are: %d, %0.0f, %o" %
      (x, answer_to_life, is_whole_number))  # mixed literals

print("My three special strings are: %s, %s, %s" %
      (x, answer_to_life, is_whole_number))  # string literals

print("My three special floats are: %f, %f, %f" %
      (x, answer_to_life, is_whole_number))  # float literals
