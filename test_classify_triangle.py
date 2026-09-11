import unittest

from classify_triangle import classify_triangle


class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")

    def test_isosceles_triangle_in_different_orders(self):
        self.assertEqual(classify_triangle(5, 8, 5), "Isosceles")
        self.assertEqual(classify_triangle(8, 5, 5), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_scalene_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")

    def test_right_triangle_in_different_orders(self):
        self.assertEqual(classify_triangle(3, 5, 4), "Scalene and Right")
        self.assertEqual(classify_triangle(5, 4, 3), "Scalene and Right")

    def test_sides_that_do_not_make_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")
        self.assertEqual(classify_triangle(1, 1, 3), "Not a triangle")

    def test_zero_side(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid input")

    def test_negative_side(self):
        self.assertEqual(classify_triangle(-3, 4, 5), "Invalid input")

if __name__ == "__main__":
    unittest.main()
