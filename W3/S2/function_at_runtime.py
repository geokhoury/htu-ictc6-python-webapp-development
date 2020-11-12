# Defining Functions at Runtime

x = 0
if x:
    def hello():
        print('Hello, World!')
else:
    def hello():
        print('Hello, Universe!')

hello()
# Prints Hello, Universe!
