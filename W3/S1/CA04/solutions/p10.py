""" 10. Given two lists of equal size create a set which contains elements from both lists as a pair.
* `first_list = [2, 3, 4, 5, 6, 7, 8]`
* `second_list = [4, 9, 16, 25, 36, 49, 64]`
* `results_set = {(2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64)}`
"""

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result_list = []
list_length = len(first_list)
i = 0

for i in range(list_length):
    my_tuple = (first_list[i], second_list[i])
    result_list.append(my_tuple)

print(sorted(set(result_list)))

# Another solution
# result_zip = list(zip(first_list, second_list))
# print(result_zip)
