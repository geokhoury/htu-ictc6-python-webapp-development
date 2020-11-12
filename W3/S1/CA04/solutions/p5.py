""" 5. Given a list of numbers, reverse the list without using the `reverse()` method.
"""

my_list = [1, 2, 3, 4, 5]
result = []

for i in my_list:
    result.insert(0, i)

print(f"{my_list} reversed is {result}")
