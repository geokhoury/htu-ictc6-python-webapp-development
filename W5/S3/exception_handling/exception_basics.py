# import module sys to get the type of exception
import sys

# > How to use a try...except block to catch exceptions?
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    try:
        print(f"n = {number} and 1/n = {1/number}\n")
    except Exception as e:
        print(f"Something went wrong! We faced an {e.__class__} error occurred.")
        print("Trying next number.\n")

# > Handling Multiple Exceptions

# try:
#    # do something
#    pass

# except ValueError:
#    # handle ValueError exception
#    pass

# except (TypeError, ZeroDivisionError):
#    # handle multiple exceptions
#    # TypeError and ZeroDivisionError
#    pass

# except:
#    # handle all other exceptions
#    pass