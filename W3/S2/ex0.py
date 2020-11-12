# Functions

# Basic structure


def say_hello():
    print("Hello, Python!")
    print("Hello, again!")


def say_hello_again(name):
    print("Hello, %s!" % name)


def say_hello_multiple(name, count):
    if count % 2 == 0:
        msg = "Hello there, {}!"
        print(msg.format(name * int(count)))
    else:
        print("Hello.")


def do_nothing():
    pass


# return_hello()
def return_hello(name):
    return "Hello, " + name + "!"

# add(num1,num2)


def add(num1, num2):
    return num1 + num2


# fancy_add(num1, num2)
def fancy_add(num1, num2):
    return num1, num2, num1 + num2

# list_from_range(n)


def list_from_range(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

# fancy_list_from_range(n)


def fancy_list_from_range(n):
    return list(range(n))


# Call say_hello()
say_hello()
say_hello()

# Call say_hello_again()
say_hello_again("HTU ICTC5!")
say_hello_again("George")
say_hello_again("Hamzah")
say_hello_again("Nadeen")

# Call say_hello_multiple()
say_hello_multiple("Moayad", 3)
say_hello_multiple("Rawan", 5)
say_hello_multiple("Obieda", 4)

# Call return_hello()
hello_msg = return_hello("George")
hello_msg = return_hello("Hamzah")
hello_msg = return_hello("Moayad")
hello_msg = return_hello("Nadeen")

print(hello_msg)

# Call add(5,4)

sum_of_numbers = add(5, 4)
print(f"The sum of the numbers is: {sum_of_numbers}")

print("The sum of the numbers is: %d" % add(5, 4))

# Call fancy_add(5,4)
a, b, sum_of_numbers = fancy_add(5, 4)
print(f"The sum of the numbers {a}, {b} is: {sum_of_numbers}")

# Call list_from_range(5)
my_list = list_from_range(5)
print(my_list)

# Call fancy_list_from_range(5)
my_list = fancy_list_from_range(5)
print(my_list)
# for i in my_list:
#     print(my_list[i])

# Call do_nothing()
do_nothing()
