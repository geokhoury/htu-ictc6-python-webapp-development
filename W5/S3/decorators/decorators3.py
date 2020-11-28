# Decorators

# Define my decorator functions
def increase(x):
    return x + 1


def decrease(x):
    return x - 1


# Define my decorated functions
def do_operation(operation, x):
    return operation(x)


# Call my decorated functions
first_opeartion = do_operation(increase, 5)
second_opeartion = do_operation(decrease, 5)

# Print the results
print(first_opeartion, second_opeartion)
