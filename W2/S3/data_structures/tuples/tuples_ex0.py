# Tuples

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

# > WWTP?
print(t1[0])    # 1
print(t1[-1])   # 4
print(t1[1])    # 2
print(t1[2])    # 3
print(t2[2])    # 7
print(t2[-1])   # 8
print(t2[0])    # 5
print(t2[-2])   # 7

# > WWTP?

t3 = t1*4 + t2  # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8)

t4 = t3 * 3     # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8,
#  1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8,
#  1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8)

# > Find the length?
print(f"t3 has {len(t3)} elements.")
print(f"t4 has {len(t4)} elements.")

# > max() and min()
print(f"In t3 the max is: {max(t3)} and the min is: {min(t3)}.")
print(f"In t4 the max is: {max(t4)} and the min is: {min(t4)}.")

# > Membership Test

# > WWTP?
print(f"Is 1 in t1? {1 in t1}")     # True
print(f"Is 2 in t2? {2 in t2}")     # False
print(f"Is 3 in t3? {3 in t3}")     # True
print(f"Is 4 in t4? {4 in t4}")     # True

print("Is 7 in t3? %s" % (7 in t3))  # True

# > Count the elements
my_number = 4
print(f"The element {my_number} appears {t4.count(my_number)} times.")
my_number = 8
print(f"The element {my_number} appears {t4.count(my_number)} times.")
my_number = 1
print(f"The element {my_number} appears {t4.count(my_number)} times.")
print(f"The element 6 appears {t4.count(6)} times.")

# > Find index
print(f"The element 8 appears at index {t4.index(8)} for the first time.")
print(f"The element 8 appears at index {t1.index(2)} for the first time.")

# > WWTP?
print("The maximum in t1 is: %d" % max(t1))     # 4
print("The minimum in t1 is: %d" % min(t1))     # 1
print("The maximum in t4 is: %d" % max(t4))     # 8
print("The minimum in t4 is: %d" % min(t4))     # 1
