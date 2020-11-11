
# Symmetric Difference

odd_list = [1, 3, 5, 7, 9]
natural_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# DO NOT CHANGE CODE ABOVE THIS LINE

# TODO:
# Print a list of the difference between the two lists.
# You cannot use the symmetric_difference() method for sets to solve this problem.
#
# For the input above, the printed list looks like this:
# >> [2, 4, 6, 8]

odd_set = set(odd_list)
natural_set = set(natural_list)

diff_odd_list = list(odd_set.difference(natural_set))
diff_natural_list = list(natural_set.difference(odd_set))

diff_list = diff_odd_list + diff_natural_list

print(sorted(diff_list))

print(list(odd_set.symmetric_difference(natural_set)))
print(list(natural_set.symmetric_difference(odd_set)))
