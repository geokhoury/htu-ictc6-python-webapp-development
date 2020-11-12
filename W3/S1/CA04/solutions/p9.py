""" 9. Given two lists of equal size, create a third list by picking an even-index element from the first list and odd-index element from second.
   * `first_list = [3, 6, 9, 12, 15, 18, 21]`
   * `second_list = [4, 8, 12, 16, 20, 24, 28]`
   * `results_list = [3, 8, 9, 16, 15, 24, 21]` 
"""

first_list = [3, 6, 9, 12, 15, 18, 21]
second_list = [4, 8, 12, 16, 20, 24, 28]

list_length = len(first_list)
results_list = []

for i in range(list_length):
    if i % 2 == 0:
        results_list.append(first_list[i])
    else:
        results_list.append(second_list[i])

print(results_list)
