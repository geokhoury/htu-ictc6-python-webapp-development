# Function Recursion

def countdown(num):
    if num <= 0:
        print('Stop')
    else:
        print(num)
        countdown(num-1)


countdown(5)
# Prints 5
# Prints 4
# Prints 3
# Prints 2
# Prints 1
# Prints Stop
