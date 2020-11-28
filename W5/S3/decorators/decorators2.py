# Decorators

def hello(name="Python"):
    print("I am hello().")

    def welcome():
        print("\t I am welcome(). Welcome to Python web!")

    def greet(name):
        print(f"\t Hello, {name}. I am greet().")

    if name == "Python":
        welcome()
    else:
        greet(name)

    print("This is the end of hello().")


# What would this do?
hello("Python")
hello("George")
