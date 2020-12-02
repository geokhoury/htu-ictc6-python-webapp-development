# Decorators

# Define my decorator function
def make_pretty(some_func):
    print("I am the decorator.")

    # Define a nested (wrapped) function
    def wrap_func(name):
        print("I will now make this name pretty.")

        # Call my decorated function with a modified parameter
        some_func(name.title())

        print("I finished calling some_func, the name is now pretty.")
    
    # Return the nested (wrapped) function
    return wrap_func


# Define my decorated functions
@make_pretty
def pretty_name(name):
    print(name)

@make_pretty
def pretty_greet(name):
    print(f"Hello, {name}!")


# Call my decorated functions
pretty_name("george")
pretty_greet("george")