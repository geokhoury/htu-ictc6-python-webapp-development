# Decorators

# Define my decorator functions
def increase(x):
    return x + 1

def decrease(x):
    return x - 1

def times_two(x):
    return x * 2

def power_two(x):
    return x ** 2

# Define my decorated functions
def do_operation(operation, x):
    return operation(x)     # return increase(5) // return decrease(5)


# Call my decorated functions
first_opeartion = do_operation(increase, 5)
second_opeartion = do_operation(decrease, 5)
third_operation = do_operation(times_two, 4)
fourth_operation = do_operation(power_two, 4)

# Print the results
print(first_opeartion, second_opeartion, third_operation, fourth_operation)
