from shape import Shape

# Polygon class


class Polygon(Shape):

    # Polygon(no_of_sides)
    def __init__(self, no_of_sides):

        # TODO: call the super __init__ method
        super().__init__()

        # keeps track of how many sides a polygon has and the sides
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def __str__(self):
        return f"I am a polygon with {self.n} sides."

    # instance methods
    def input_sides(self):
        # ask the user for input based on the number of sides for the polygon
        # if you are not sure what it does, call this method!
        self.sides = [float(input("Enter side "+str(i+1)+" : "))
                      for i in range(self.n)]

    def display_sides(self):
        for i in range(self.n):
            # prints the sides of any given polygon
            print("Side", i+1, "is", self.sides[i])
