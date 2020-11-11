# Flow Control - Decisions

x = -20
y = 42
z = -2

# if statements

if x > 0:
    print("Found a positive number.")
    print(f"{x} is greater than zero.")
print("I will print this anyway.")

# if...else statements

if x < 0:
    print(f"{x} is a negative number.")
    print("I belong to the if.")
else:
    print(f"{x} is a positive number.")
    print("I belong to the else.")

# Evaluate this

x, y, z = 10, 60, 0

if (x == 5 or y == 20):
    print(f"x: {x} y: {y}. Either x == 5 or y == 20.")
else:
    print(f"x: {x} y: {y}. Niether x == 5 nor y == 20.")

# Evaluate this

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}  # Set
number_to_check = 12

if number_to_check in prime_numbers:
    print("The number %d is a prime number." % number_to_check)
else:
    print("The number %d is not a prime number." % number_to_check)

# Short hand if - One statement blocks

a, b = 4, 3
if a > b:
    print("a is greater than b")

# Short hand if..else - One statement blocks

# [true one statement block] if expression else [false one statement block]
print("A is greater.") if a > b else print("B is greater.")

# Same as the short hand form above
if a > b:
    print("A is greater.")
else:
    print("B is greater.")

# if..elif..else statements

# Evaluate this
x = 1

if x < 0:
    print(f"{x} is a negative number.")
elif x == 0:
    print(f"{x} is a zero.")
else:
    print(f"{x} is a positive number.")

# if..elif..else statements

# Evaluate this
# x = -20

# if x < 0:
#     print(f"{x} is a negative number.")
# elif x == 0:
#     print(f"{x} is a zero.")
# elif x % 2 == 0:
#     print(f"{x} is an positive even number.")
# else:
#     print(f"{x} is a positive odd number.")


# # Nested if..elif..else statements

# # Evaluate this

# # Read input from stdin and cast to float
# number = float(input("Enter a number: "))

# # Check if number is positive
# if number >= 0:
#     # Check if number is zero
#     if number == 0:
#         print(f"{number} is zero.")
#     else:
#         print(f"{number} is a positive number.")
# # Check if number is negative
# else:
#     print(f"{number} a negative is number.")

# if..elif..else statements

# Evaluate this
x = -2

if x > 0:
    print("I will print this.")
elif x == 2 or x == -2:
    print("I will print this too.")
else:
    print("I will never print this.")

# > if..elif..else statements

# Evaluate this
x = -1

# if (x > 0 and x % 2 == 0):
#     print(f"{x} is positive and even.")
# elif (x < 0 and x % 2 == 0):
#     print(f"{x} is negative and even.")
# elif (x < 0 and x % 2 != 0):
#     print(f"{x} is negative and odd.")
# else:
#     print(f"{x} is positive and odd.")

# > Nested if statements

if x > 0:
    print(f"{x} is positive and even.") if x % 2 == 0 else print(
        f"{x} is positive and odd.")
else:
    print(f"{x} is negative and even.") if x % 2 == 0 else print(
        f"{x} is negative and odd.")

# Evaluate this
x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
