import sys
import os
from typing import List, Tuple
import unittest

"""
This file contains test cases for the check_location_is_within_area function
Contains general cases, plus some edge cases
check_location_is_within_area runs in O(n) time, and passes 6/6 test cases
"""

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from utils import check_location_is_within_area

class TestRayCasting(unittest.TestCase):
    # General test cases
    def testPointInsideArea(self):
        location = (0.5, 0.5)
        area = [(0, 0), (1, 0), (1, 1), (0, 1)]
        self.assertTrue(check_location_is_within_area(location, area))

    def testPointOutsideArea(self):
        location = (1.5, 1.5)
        area = [(0, 0), (1, 0), (1, 1), (0, 1)]
        self.assertFalse(check_location_is_within_area(location, area))

    def testPointInsideAreaComplexPolygon(self):
        location = (2, 2)
        area = [(0, 0), (4, 0), (4, 4), (2, 6), (0, 4)]
        self.assertTrue(check_location_is_within_area(location, area))

    def testPointOutsideAreaComplexPolygon(self):
        location = (5, 5)
        area = [(0, 0), (4, 0), (4, 4), (2, 6), (0, 4)]
        self.assertFalse(check_location_is_within_area(location, area))

    # Edge test cases
    def testPointOnEdge(self):
        location = (0.5, 0)
        area = [(0, 0), (1, 0), (1, 1), (0, 1)]
        self.assertTrue(check_location_is_within_area(location, area))

    def testPointOnEdgeComplexPolygon(self):
        location = (2, 0)
        area = [(0, 0), (4, 0), (4, 4), (2, 6), (0, 4)]
        self.assertTrue(check_location_is_within_area(location, area))

if __name__ == '__main__':
    unittest.main()
