from bird import Bird

import random
# Parrot class (child)

class Parrot(Bird):

    # Call __init__() method for the Parrot object
    def __init__(self, name, age):

        # Call super().__init__() function
        super().__init__(name, age)

        # Instance attribute
        self.level = int(random.random()*10)
        self.has_birthday_today = False

        # WWTP?
        print(self)

    # string representation
    def __str__(self):
        # Call the __str__() method from the parent class
        print(super().__str__())

        # return the parrot
        return f'''
        \\\\
        (o>
        //\\
        V_/__
        ||
        ||\n\n This is {self.name}, {self.age} years old. \n\n'''

    # instance methods

    # > Overriding the dance() method from the parent class
    def dance(self):
        print(f"{self.name} has reached level {self.level} at dancing.")
        if self.level > 7:
            print(f"{self.name} is dancing a special dance.")
        else:
            # Call the dance() method from the parent class
            super().dance()

    # > Overriding the eat() method from the parent class
    def eat(self, food): 
        print(f"'{self.name}' thinks that '{food}' is yummy.")
        
        # Call the eat(food) method from the parent class
        super().eat(food)

    # > Overriding the fly() method from the parent class
    def fly(self):
        print(f"My parrot '{self.name}' is flying!")

    # > 
    def celebrate_birthday(self):
        # This generates a random float between 0.0 and 1.0
        rnd_bday = random.random()

        # If the chance is greater than 0.5
        if rnd_bday > 0.5:
            self.has_birthday_today = True

        if self.has_birthday_today:
                print(f"It is {round(rnd_bday*100)} % your birthday today. Happy birthday!")
                self.age += 1
                print(f"You are now {self.age} years old.")
                self.eat("cake")
                self.dance()
        else:
            print(f"It is only {round(rnd_bday*100)}% that it is my birthday today.")
            print("I guess this means no cake.")


