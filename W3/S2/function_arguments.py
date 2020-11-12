# Function Arguments

# > Positional Arguments

# def print_job(name, job):
#     print(name, 'is a', job)


# print_job('Bob', 'developer')
# # Prints Bob is a developer

# > Keyword Arguments


# def print_job(name, job):
#     print(name, 'is a', job)


# print_job(name='Bob', job='developer')
# print_job(job='developer', name='Bob')

# # Prints Bob is a developer

# print_job(job='developer', name='Bob')
# # Prints Bob is a developer

# > Default Arguments

def print_job(name, job='developer'):
    print(name, 'is a', job)


print_job('Bob', 'manager')
# Prints Bob is a manager

print_job('Bob')
# Prints Bob is a developer

# > Variable Length Positional Arguments


def print_numbers(*numbers):
    print(numbers)


print_numbers(1, 54, 60, 8, 98, 12, 42, 24)
# Prints (1, 54, 60, 8, 98, 12)

# > Variable Length Keyword Arguments


def print_info(**kwargs):
    print(kwargs)


print_info(name='Bob', age=25, job='dev', company='Google')
# Prints {'name': 'Bob', 'age': 25, 'job': 'dev', 'company': 'Google'}
