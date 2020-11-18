# Class Dog

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
        self.eye_color = None
        self.hair_color = 'brown'

    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in respon  se to a command."""
        print(f"{self.name} rolled over!")
    
    def print_dog(self):
        print(f"The dog is called {self.name} and is {self.age} years old.")
        print(f"{self.name} has {self.eye_color} eyes and {self.hair_color} hair.")

# Making an Instance from a Class (instantiation)
rex = Dog('Rex', 6)
your_dog = Dog('Lucy', 3)
my_dog = Dog('LV', 2)

# Accessing Attributes

print(f"The dog's name is {rex.name}.")
print(f"The dog is {rex.age} years old.")

# Setting attributes
rex.eye_color = 'blue'
print(f"{rex.name} has {rex.eye_color} eyes.")

rex.hair_color = 'white'
print(f"{rex.name} has {rex.hair_color} hair.")

# On-the-fly attributes
rex.has_glasses = True
print(f"Does {rex.name} have glasses? {rex.has_glasses}")

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
print(f"Your dog has {your_dog.hair_color} hair.")

your_dog.eye_color = 'black'
print(f"Your dog has {your_dog.eye_color} eyes.")

print(f"My dog is called {my_dog.name} and is {my_dog.age} years old.")
my_dog.hair_color = 'black'
print(f"My dog has {my_dog.hair_color} hair.")
# print(f"Does {my_dog.name} have glasses? {my_dog.has_glasses}") # my_dog has not attribute 'has_glasses'

# Calling methods
rex.sit()
rex.roll_over()

your_dog.sit()
your_dog.roll_over()

rex.print_dog()
my_dog.print_dog()
your_dog.print_dog()