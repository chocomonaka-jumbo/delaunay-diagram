import unittest
import delaunay2


class TestDelaunayDiagram(unittest.TestCase):
    """test class of delaunay.py
    """
    
    def test_getRandom2DPoints(self):
        """test method for getRandom2DPoints"""
        test_width = 100
        test_height = 100
        test_n = 50
        
        expected = (test_n, 3)
        result = delaunay2.getRandom2DPoints(test_width, test_height, test_n)
        self.assertEqual(expected, result.shape)
    
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