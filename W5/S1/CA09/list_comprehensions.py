
# Declare a variables squares
squares = []

# > Build the squares list using a loop
for x in range(10):
    squares.append(x**2)

# Squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# > Build the squares list using a list comprehension
squares = [x**2 for x in range(10)]

# Squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]