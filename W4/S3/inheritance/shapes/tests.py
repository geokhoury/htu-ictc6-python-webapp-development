import unittest
import logging

from shape import Shape
from circle import Circle
from square import Square
from polygon import Polygon


class CircleTest(unittest.TestCase):

    def test_shape(self):
        self.assertIsInstance(Circle(), Circle)

    def test_find_area(self):
        circle = Circle(15)
        self.assertEqual(circle.find_area(), 706.5)

    def test_find_circumference(self):
        circle = Circle(15)
        self.assertEqual(circle.find_circumference(), 94.2)

    def test(self):
        self.assertTrue(True)


class SquareTest(unittest.TestCase):

    def test_find_area(self):
        square = Square(2, 2)
        self.assertEqual(square.find_area(), 4)

    def test_find_perimeter(self):
        square = Square(2, 2)
        self.assertEqual(square.find_perimeter(), 8)


class PolygonTest(unittest.TestCase):

    def test_inheritance(self):
        self.assertIsInstance(Polygon(2), Polygon)
        self.assertIsInstance(Polygon(2), Shape)

    def test_str(self):
        polygon = Square(2, 2)
        self.assertIsInstance(polygon.__str__(), str)


if __name__ == '__main__':
    unittest.main()
