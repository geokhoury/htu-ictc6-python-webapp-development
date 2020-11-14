# > Local scope

def myfunc():
    x = 42      # local scope x
    print(x)

myfunc()        # prints 42
# print(x)        # NameError: name 'x' is not defined
