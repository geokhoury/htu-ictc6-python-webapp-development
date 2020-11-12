"""1. Write a program which reads a number `(n)` from the user and the print the sum of all numbers between `1` and `n`. 
"""

n = int(input("Please enter a number: "))
print(f"The sum of the number between 1 and {n} is {sum(range(1, n+1))}.")
