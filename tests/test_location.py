import unittest
from location import Location

"""""
This file contains test cases for the Location class.
It includes tests for initializing the location, setting and getting the longitude and latitude.
"""""

class TestLocation(unittest.TestCase):
    def setUp(self):
        # Initialize a Location object with initial longitude and latitude
        self.location = Location(30, 45)

    def test_inital_longitude(self):
        # Test the initial longitude value
        self.assertEqual(self.location.get_longitude(),30)

    def test_inital_latitude(self):
        # Test the initial latitude value
        self.assertEqual(self.location.get_latitude(),45)

    def test_set_longitude(self):
        # Test setting a new longitude value
        self.location.set_longitude(35)
        self.assertEqual(self.location.get_longitude(),35)

    def test_get_longitude(self):
        # Test getting the updated longitude value
        self.location.set_longitude(40)
        self.assertEqual(self.location.get_longitude(),40)

    def test_set_latitude(self):
        # Test setting a new latitude value
        self.location.set_latitude(50)
        self.assertEqual(self.location.get_latitude(),50)

    def test_get_latitude(self):
        # Test getting the updated latitude value
        self.location.set_latitude(55)
        self.assertEqual(self.location.get_latitude(),55)

    def test_location(self):
        # Test setting both longitude and latitude, and then getting their values
        self.location.set_longitude(55)
        self.location.set_latitude(60)
        self.assertEqual(self.location.get_longitude(),55)
        self.assertEqual(self.location.get_latitude(),60)

if __name__ == '__main__':
    unittest.main()