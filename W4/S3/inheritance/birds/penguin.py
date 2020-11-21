
from bird import Bird

import random

# Define a function in this module.
# Remember that this function is defined outside the class

def find_older(penguin1, penguin2):
    if penguin1.age > penguin2.age:
        return penguin1
    else:
        return penguin2

# Penguin class (child)

class Penguin(Bird):

    # Call __init__() method for the Penguin object
    def __init__(self, name, age):

        # Call super().__init__() function
        super().__init__(name, age)

        # TODO: Add additional attibutes from this class
        self.type = ''
        self.friends = []

        # Print the penguin
        print("A new penguin waddless in.")

    # Instance methods

    # > Define the run() method
    def run(self):
        print("{self.name} is running. Waddle. Waddle.")

    # > Define the find_krill() method
    def find_krill(self):
        # This generates a random float between 0.0 and 1.0
        chance_for_krill = random.random()

        if chance_for_krill > 0.3:
            print("<>< <>< <><")
            super().eat("krill")
        else:
            print("No fish today!")

    # > Define the befriend() method
    def befriend(self, friend):
        print(f"{self.name} is now friends with {friend.name}.")
        self.friends.append(friend)

        print("We are going to find krill.")
        self.find_krill()
        friend.find_krill()
    
    # > Define the print_friends() method
    def print_friends(self):
        print(f"{self.name} has {len(self.friends)} friends.")
        for friend in self.friends:
            print(f"\t * {friend.name.title()}")

    # > Overriding the fly() method from the parent class
    def fly(self):
        print("I am a penguin! I cannot fly.")
