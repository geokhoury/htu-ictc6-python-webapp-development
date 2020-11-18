# Class Parrot

class Parrot:

    # > Class attribute
    species = "bird"

    # __init__ method
    def __init__(self, name, age):
        # > Instance attribute
        self.name = name
        self.age = age
        self.color = ""
        self.has_flat_beak = False
        self.allowed_foods = ["seeds", "nuts", "grapes"]

    def __str__(self):
        return f'''
 \\\\
 (o>
 //\\
_V_/__
 ||
 ||\n\n This is {self.name}, {self.age} years old. \n\n'''

 # instance method

    def sing(self, song):
        print(f"{self.name} sings '{song}'.")

    def dance(self):
        return f"{self.name} is now dancing."

    def change_color(self, color):
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        if self.color == "":
            return f"{self.name} has not color."
        else:
            return self.color

    def eat(self, food):
        if food in self.allowed_foods:
            print(f"{self.name} is eating {food}.")
        else:
            print(f"Yuck! {self.name} does not eat {food}.")

    def celebrate_birthday(self):
        print(f"I am {self.name}. I am {self.age} years old.")
        if self.age > 3:
            # Add 'cake' to the list of allowed foods.
            self.allowed_foods.append("cake")

            # Call the eat('cake') method.
            self.eat("cake")

            # Increment age.
            self.age += 1
            print("Happy birthday. Yummy cake!")
        else:
            print("Haha! Nice try, maybe next year.")


# > Create two instances of the Parrot class
blu = Parrot("Blu", 2)
woo = Parrot("Woo", 4)

# > Access the attributes
print(f"{blu.name} is a {blu.species}.")
print(f"{woo.name} is a {woo.species}.")

# > Modifying the attributes (instance)
woo.age = 5
woo.has_flat_beak = True
blu.age = 3

# > Access the attributes
print(f"{blu.name} is {blu.age} years old.")
print(f"{woo.name} is {woo.age} years old.")

# > Modifying the attributes (on-the-fly instance)
blu.species = 'parrot'

print(Parrot.species)                       # prints the class attribute

# > Access the attributes
print(f"{blu.name} is a {blu.species}.")    # prints the instance attribute
print(f"{woo.name} is a {woo.species}.")    # prints the class attribute

# > Changing attribute values
blu.color = "Red"                           # Direct changing an instance attribute
blu.change_color("White")                   # Calling a method like change_color(color)

print(blu.color)

# > Calling the instance methods

blu.sing("I love you")
woo.sing("Happy")
print(blu.dance())
print(woo.dance())

# > Call eat()
blu.eat("grapes")                           # eat "grapes"
blu.eat("seeds")                            # eat "seeds"

woo.allowed_foods = ["seeds"]               # Override the list of what what woo can eat
woo.eat("seeds")                            # Woo is eating seeds.
woo.eat("grapes")                           # Yuck! Woo does not eat grapes.

# > Call celebrate_birthday()
blu.celebrate_birthday()                    # Blu is 3 years old. Cannot eat cake.
woo.celebrate_birthday()                    # Woo celebrates birthday.

# Check if the same instance
a = blu
b = woo

if a == b:
    print(f"{a} is {b}.")

    print(f"{a.name} is ({id(a)}) is of type {type(a)}.")
    print(f"{b.name} is ({id(b)}) is of type {type(b)}.")

else:
    print(f"{a} is not {b}.")

    print(f"{a.name} - ({id(a)}) is of type {type(a)}.")
    print(f"{b.name} - ({id(b)}) is of type {type(b)}.")

# Call the __str__() method
print(woo)
print(blu) 