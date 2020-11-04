# F literal strings in Python

my_name = 'Nicola Tesla'
my_age = 86  # Born 1856 and died 1943
my_height = 1.88  # m
my_weight = 64    # Kg
my_eyes = 'black'
my_hair = 'brown'

print(f"Let us talk about {my_name}.")
print(f"He is {my_height} m tall.")
print(f"He is {my_weight} Kg heavy.")
print("Actually that's not too heavy.")

print(f"He's got {my_eyes} eyes and {my_hair} hair.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
