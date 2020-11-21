# Shape class


class Shape:
    def __init__(self):
        print("A new shape has been created.")

    # overriding the str() for shape
    def __str__(self):
        return "I am a shape."
