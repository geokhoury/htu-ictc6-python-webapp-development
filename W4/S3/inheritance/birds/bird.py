# Bird class (parent)
class Bird:

    # class attribute
    species = "bird"

    # __init__ method for the Bird object
    def __init__(self, name, age):
        print("A new bird is in the sky.")

        # instance attribute

        self.name = name
        self.age = age

    def __str__(self):
        return f"This is a bird. Called '{self.name}'."

    # instance methods

    def who_is_this(self):
        print(f"Who else? {self.name}!")

    def fly(self):
        print(f"'{self.name}' is soaring high.")

    def dance(self):
        print(f"'{self.name}' is now dancing.")

    def sing(self, song):
        print(f"'{self.name}' sings '{song}''.")

    def eat(self, food):
        print(f"'{self.name}' is eating '{food}'.")
