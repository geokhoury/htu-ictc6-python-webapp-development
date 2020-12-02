from datetime import datetime

# Define my decorator
def print_with_dt(my_say_hello_func):
    # Define my inner (nested or wrapped) function
    def my_inner_func():
        # Call the function we wish to decorate
        my_say_hello_func()

        # Print the current timestamp
        print(f"The current timestamp is: {datetime.now()}")

    # Return my decorated function
    return my_inner_func

# Define a function to decorate
@print_with_dt
def say_hello():
    print("Hello, Hamza!")

@print_with_dt
def global_print():
    print("I am a global message")

# Call the function
say_hello()
global_print()

