# Function Return

# > Return a single value

# Return addition of the arguments


def add(a, b):
    return a+b
    print("I will never get here.")


result = add(3, 2)
print(result)
# Prints 5

# > Return multiple value

# Unpack returned tuple


# def do_math(a, b):
#     return a+b, a-b


# add, sub = do_math(3, 2)

# print(add)
# # Prints 5
# print(sub)
# # Prints 1

# # > Return multiple value

# # Unpack returned tuple


# def do_math(a, b):
#     return a+b, a-b


# add, sub = do_math(3, 2)

# print(add)
# # Prints 5
# print(sub)
# # Prints 1


# > Return multiple value

# Unpack returned tuple


def do_math(a, b):
    return a+b, a-b, a*b, a//b


add, sub, mul, div = do_math(3, 2)

print(add)
# Prints 5
print(sub)
# Prints 1
print(mul)
# Prints 6
print(div)
# Prints 1

print(do_math(3, 2))
# Prints (5,1,6,1)
