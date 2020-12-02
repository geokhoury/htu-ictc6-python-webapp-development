# Errors and Exceptions

# # > Without exception handling
# number = int(input("Please enter a number: "))
# print(f"3 divided by {number} is {3 / number}") 
# print("Goodbye!")

# > With an if...else statement
# number = int(input("Please enter a number: "))
# if number == 0:
#     print("Dividing by zero is not allowed.")
# else:
#     print(f"3 divided by {number} is {3 / number}")
# print("Goodbye!")

# > With a try...except clause
# number = int(input("Please enter a number: "))
# try:
#     print(f"3 divided by {number} is {3 / number}") 
# except:
#     print("Dividing by zero is not allowed.")
# print( "Goodbye!" )

# > Handling specific exceptions
try:
    number = int(input("Please enter a number: "))
    print(f"3 divided by {number} is {3 / number}")
except ZeroDivisionError:
    print("Dividing by zero is not allowed.")
except ValueError:
    print("The value you entered is not an integer.")
print("Goodbye!")