# Decorators

# Define my decorator function
def make_pretty(some_func):
    def wrap_func(name):
        print("I will now make this name pretty.")
        some_func(name.capitalize())
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
