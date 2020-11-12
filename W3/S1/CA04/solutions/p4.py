""" 4. Given a list of numbers iterate over it and print numbers which are divisible by `5`. 
If you find number greater than `150` stop and exit iteration.
"""

my_list = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]

print(f"My list has {len(my_list)} numbers.")

for number in my_list:
    if number <= 150 and number % 5 == 0:
        print(number)
    else:
        print("Stopping")
        break
