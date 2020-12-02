# Decorators

def hello(name="Python"):
    # Print
    print("I am hello().")

    # Define a nested function (local for hello())
    def welcome():
        print("\t I am welcome(). Welcome to Python web!")

    # Define a nested function (local for hello())
    def greet(greet_name):
        print(f"\t Hello, {greet_name}. I am greet().")

    if name == "Python":
        # Call welcome()
        welcome()
    else:
        # Call greet() with the value name from hello()
        greet(name)

    print("This is the end of hello().")

# What would this do?
hello()
hello("George")
