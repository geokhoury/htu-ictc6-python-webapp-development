# Global Scope

# > Acessing a global variable

x = 42          # global scope x

def myfunc():
    x = 0
    print(f"I am the local x = {x}.")    # local x is 0

myfunc()
print(f"I am the global x = {x}.")        # global x is still 42

# > Modifying a global variable

x = 42          # global scope x
y = 24
def my_global_func():
    global x    # declare x global
    x = 0
    print(f"I am the global x = {x}.")    # global x is now 0
    x = 10
    print(f"I am the global x = {x}.")    # global x is now 10

my_global_func()
print(f"I am the global x = {x}.")        # global x is 10