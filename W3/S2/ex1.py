# Functions

# Min / Max


def minimum(x, y):
    if x < y:
        return x
    return y


def maximum(x, y):
    if x > y:
        return x
    return y

# Calcualte the length of the string


def get_length(some_string):
    count = 0
    for c in some_string:
        count = count + 1  # count += 1
    return count  # Note the block indentation!

# Enumerate lists


def pretty_print(my_list):
    for i, v in enumerate(my_list):
        print(f"{i}: {v}")

    index = 0
    for v in my_list:
        print(f"{index}: {v}")
        index += 1

# join_with()

# list = ["a", "b", "c"]
# special = "**"

# a**b**c


def join_with(my_list, special_string):
    output = "A**B**C"
    for i, v in enumerate(my_list):  # i = 2 v = C
        output = output + v
        if i != len(my_list) - 1:
            output = output + special_string
    return output

    # output_list = []
    # for i, v in enumerate(my_list):
    #     output_list.append(v)
    #     if i != len(my_list) - 1:
    #         output_list.append(special_string)
    # return output_list

    # def join_with(my_list, special_string):
    #     return special_string.join(my_list)

# is_secret(secret_text) - Returns True if string is the word 'secret' is in the string


def is_secret(secret_text):
    if 'secret' in secret_text:
        return True
    return False

# make_code(clear_string) - Returns a copy of the string with all vowels replaced with 'x'


def make_code(clear_string):
    vowels = "aeiou"
    result = list(clear_string)

    for i, c in enumerate(clear_string):
        if c in vowels:
            result[i] = "x"

    return "".join(result)

    # for i in clear_string:
    #     if i in vowels:
    #         result = clear_string.replace(i, "x")


# Main
# Calls for min(), max()
min_number = minimum(1, 2)  # min()
max_number = maximum(10, 2)  # max()

# Call the built-in function min()
min_builtin = min(2, 3)

print(min_number, max_number, min_builtin)


# Call the get_length()

text = "Some textual string"
print(f"The number of characters in the string: '%s' is: %d." %
      (text, get_length(text)))  # len()

print(f"The number of characters in the string: '%s' is: %d." %
      (text, get_length(text)))

# count for the first time ## 19
get_length("one...19")

# count for the second time  ## 5
get_length("12345")

# Call pretty_print()
my_list = [2, 4, 6, 8]
pretty_print(my_list)

# Call join_with()
my_special_string = join_with(["A", "B", "C"], "**")
print(my_special_string)

# Call is_secret()
secret_text = "This text is a secret."
print("It is %s that 'secret' is in: '%s'." %
      (is_secret(secret_text), secret_text))

if is_secret("mysecretpassword"):
    print("Safe password!")

# Call make_code()
print(make_code("Some string with vowels."))
