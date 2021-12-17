import unittest
import delaunay3
import numpy as np

class TestDelaunayDiagram(unittest.TestCase):
    """test class of delaunay.py
    """
    
    def test_getRandom2DPoints(self):
        """test method for getRandom2DPoints"""
        test_width = 100
        test_height = 100
        test_n = 50
        
        expected = (test_n, 3)
        result = delauney3.getRandom2DPoints(test_width, test_height, test_n)
        self.assetEqual(expected, result.shape)
    
    

if __name__ == "__main__":
    unittest.main()