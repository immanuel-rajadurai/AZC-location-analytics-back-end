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
from src.utils import check_location_is_within_area
from src.location import Location
from src.area import Area

class TestRayCasting(unittest.TestCase):
    # General test cases
    def testPointInsideArea(self):
        location = Location(0.5, 0.5)
        a1 = Area("Test Area", [Location(0, 0), Location(1, 0), Location(1, 1), Location(0, 1)])
        area = a1.get_geofence()
        self.assertTrue(check_location_is_within_area(location, area))

    def testPointOutsideArea(self):
        location = Location(1.5, 1.5)
        a1 = Area("Test Area", [Location(0, 0), Location(1, 0), Location(1, 1), Location(0, 1)])
        area = a1.get_geofence()
        self.assertFalse(check_location_is_within_area(location, area))

    def testPointInsideAreaComplexPolygon(self):
        location = Location(2, 2)
        a1 = Area("Complex Area", [Location(0, 0), Location(4, 0), Location(4, 4), Location(2, 6), Location(0, 4)])
        area = a1.get_geofence()
        self.assertTrue(check_location_is_within_area(location, area))

    def testPointOutsideAreaComplexPolygon(self):
        location = Location(5, 5)
        a1 = Area("Complex Area", [Location(0, 0), Location(4, 0), Location(4, 4), Location(2, 6), Location(0, 4)])
        area = a1.get_geofence()
        self.assertFalse(check_location_is_within_area(location, area))

    # Edge test cases
    def testPointOnEdge(self):
        location = Location(0.5, 0)
        a1 = Area("Test Area", [Location(0, 0), Location(1, 0), Location(1, 1), Location(0, 1)])
        area = a1.get_geofence()
        self.assertTrue(check_location_is_within_area(location, area))

    def testPointOnEdgeComplexPolygon(self):
        location = Location(2, 0)
        a1 = Area("Complex Area", [Location(0, 0), Location(4, 0), Location(4, 4), Location(2, 6), Location(0, 4)])
        area = a1.get_geofence()
        self.assertTrue(check_location_is_within_area(location, area))

if __name__ == '__main__':
    unittest.main()