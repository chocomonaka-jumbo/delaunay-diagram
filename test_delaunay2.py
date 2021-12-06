import unittest
import delaunay2
import numpy as np

class TestDelaunayDiagram(unittest.TestCase):
    """test class of delaunay.py
    """

    def test_get_color(self):
        """test method for get_color
        """
        value1 = 10
        value2 = 10
        value3 = 10
        expected = (50,0,200)
        actual = delaunay2.get_color(value1, value2, value3)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()