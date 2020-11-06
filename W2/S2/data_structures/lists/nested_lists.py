# Nested lists

numbers = [1, [2, 2], [3, 3, 3], [4, 4, 4, 4]]

print(numbers[0], type(numbers[0]))
print(numbers[1], type(numbers[1]))
print(numbers[2], type(numbers[2]))
print(numbers[3], type(numbers[3]))

# looking into numbers[1]
print(numbers[1], type(numbers[1]))

print(numbers[1][0], type(numbers[1][0]))
print(numbers[1][1], type(numbers[1][1]))

# looking into numbers[2]
print(numbers[2], type(numbers[2]))

print(numbers[2][0], type(numbers[2][0]))
print(numbers[2][1], type(numbers[2][1]))
print(numbers[2][2], type(numbers[2][2]))
