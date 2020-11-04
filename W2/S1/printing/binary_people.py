# Formatted printing in Python

# declare some variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# some printing
print(x)    # WWTP?
print(y)    # WWTP?

print(f"I said: {x}")           # WWTP?
print(f"I also said: '{y}'.")   # WWTP?

# declare variables
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

liked_it = False
joke_evaluation_again = "Isn't that joke so funny?! {0}. Did you like it? {1}"
print(joke_evaluation_again.format(hilarious, liked_it))


# String concatination
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)    # WWTP?
