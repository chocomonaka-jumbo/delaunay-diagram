#python3 -m unittest discover"

import unittest
import delaunay3

class TestDelaunayDiagram(unittest.TestCase):
    """test class of delaunay3.py
    """
    
    def test_hsv_to_rgb(self):
        """test method for hsv_to_rgb"""
        test_h = 0
        test_s = 255
        test_v = 255
        
        expected = (0, 0, 255)
        result = delaunay3.hsv_to_rgb(test_h, test_s, test_v)
        self.assertEqual(expected, result)
    
    def test_get_color(self):
        """test method for get_color"""
        test_a1 = 0
        test_a2 = 15
        test_a3 = 21
        test_ave = 14
        test_ave_max = 18
        test_ave_min = 12
        
        expected = (255,215,215)
        result = delaunay3.get_color(test_a1, test_a2, test_a3, test_ave, test_ave_max, test_ave_min)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()