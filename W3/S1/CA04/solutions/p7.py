""" 7. Write a program which reads the age of 3 different people. Then print the oldest, and youngest between them.
"""

# Read three values space seperated
a1, a2, a3 = [int(a) for a in input("Enter any 3 numbers: ").split()]

ages_list = [a1, a2, a3]

print(f"The oldest person is {max(ages_list)} years old.")
print(f"The youngest person is {min(ages_list)} years old.")
