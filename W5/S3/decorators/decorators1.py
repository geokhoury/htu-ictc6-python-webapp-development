# Decorators

def hello():
    return "Hello!"


# What would this do?
print(hello())
print(hello)

# We can also assign functions to variables
greet = hello       # Note that hello is a function
print(greet())      # We can execute this function
print(greet)

# What would this do?
# del hello
# hello()
# greet()
