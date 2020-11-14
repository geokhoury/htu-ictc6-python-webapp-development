# Enclosing Scope

# > Enclosing function
def f1():
    x = 42
    # Nested function
    def f2():
        x = 0
        print(f"I am in f2 and my value is {x}.")    # x is 0
    f2()
    print(f"I am in f1 and my value is {x}.")        # x is still 42

f1()


# > Enclosing function
def g1():
    x = 42
    # Nested function
    def g2():
        nonlocal x
        x = 0
        print(f"I am in g2 and my value is {x}.")    # x is now 0
    g2()
    print(f"I am in g1 and my value is {x}.")        # x remains 0
    
g1()