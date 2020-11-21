from polygon import Polygon

# Square class


class Square(Polygon):
    def __init__(self, length, width):
        super().__init__(2)
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * self.length + 2 * self.width
