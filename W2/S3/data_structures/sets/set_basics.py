# Set Basics

# > Creating a set
s = {1, 2, 3}
print(f"'s' is of the type {type(s)} and contains: {s}.")

# > Adding elements
print(s)
s.add(4)
s.add(5)
s.add(6)
s.add(4)
s.add(6)
print(s)  # {1, 2, 3, 4, 5, 6}

# > Get the length
print(f"The set 's' contains {len(s)} elements.")  # 6

# > Membership test
print("Is 3 a member of 's'? %s" % (3 in s))
print("Is 16 not a member of 's'? %s" % (16 not in s))

# > Copy a set
another_s = s.copy()
print(f"S: {s}")            # {1, 2, 3, 4, 5, 6}
print(f"Another S: {another_s}")    # {1, 2, 3, 4, 5, 6}

# > Remove an element
s.discard(4)
print(f"S: {s}")            # {1, 2, 3, 5, 6}

# > Pop an element
print(f"S: {s}")            # {1, 2, 3, 5, 6}
value = s.pop()
print(f"Got the value {value}.")

# > Difference between sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

x = set1.difference(set2)
print(x)  # {1}

y = set2.difference(set1)
print(y)  # {4}

# > Intersection of sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

x = set1.intersection(set2)
print(x)  # {2,3}

y = set2.intersection(set1)
print(y)  # {2,3}

# > Union of sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

x = set1.union(set2)
print(x)  # {1,2,3,4}

y = set2.union(set1)
print(y)  # {1,2,3,4}
