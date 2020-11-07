# Dictionary Methods

# Create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Removes a particular item, returns its value
print(squares.pop(4))  # 16
print(squares.pop(5))  # 25

# Print the dictionary
print(squares, type(squares))  # Output: {1: 1, 2: 4, 3: 9, 5: 25}

# Pop the last element in the dictionary returns (key,value)
item = squares.popitem()
item_key, item_value = item

print(item, type(item))  # (3, 9)
print(item_key, type(item_key))  # 3, int
print(item_value, type(item_value))  # 9, int

print(squares)  # Output: {1: 1, 2: 4, 3: 9}

# Remove all items from the dictionary
squares.clear()
print(squares)  # Output: {}

# Delete the dictionary reference
# del squares

# Throws an error since `square` is no longer defined
# print(squares)
