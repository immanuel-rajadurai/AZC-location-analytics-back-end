import unittest
from src.location import Location
from src.area import Area, Restaurant, Exhibit

"""
This file contains test cases for the Area, Restaurant, and Exhibit classes.
It includes tests for initializing objects, adding and removing locations, setting and getting attributes, and checking the state of exhibits.
"""

class TestArea(unittest.TestCase):
    def setUp(self):
        # Initialize Location and Area objects
        self.location1 = Location(10, 20)
        self.location2 = Location(15, 25)
        self.area = Area("Park",[self.location1, self.location2])

    def test_add_location(self):
        # Test adding a new location to the area's geofence
        new_location = Location(30,30)
        self.area.add_location(new_location)
        self.assertIn(new_location, self.area.get_geofence())

    def test_remove_location(self):
        # Test removing a location from the area's geofence
        self.area.remove_location(self.location2)
        self.assertNotIn(self.location2, self.area.get_geofence())

    def test_get_geoference(self):
        # Test getting the list of locations in the area's geofence
        self.assertEqual(self.area.get_geofence(), [self.location1, self.location2])


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        # Initialize Location and Restaurant objects
        self.location1 = Location(10, 20)
        self.location2 = Location(15, 25)
        self.restaurant = Restaurant("La Brasserie", [self.location1, self.location2], "Takeaway")

    def test_set_restaurant_type(self):
        # Test setting the restaurant type
        self.restaurant.set_restaurant_type("Dine-in")
        self.assertEqual(self.restaurant.get_restaurant_type(), "Dine-in")

    def test_get_restaurant_type(self):
        # Test getting the restaurant type
        self.assertEqual(self.restaurant.get_restaurant_type(), "Takeaway")

    def test_add_menu_item(self):
        # Test adding an item to the restaurant's menu
        self.restaurant.add_menu_item("French fries")
        self.assertIn("French fries", self.restaurant.get_menu())

    def test_get_menu(self):
        # Test getting the restaurant's menu
        self.assertEqual(self.restaurant.get_menu(),[])


class TestExhibit(unittest.TestCase):
    def setUp(self):
        # Initialize Location and Exhibit objects
        self.location1 = Location(10, 20)
        self.location2 = Location(15, 25)
        self.exhibit = Exhibit("Giraffe Exhibit", [self.location1, self.location2], "Giraffe", True)

    def test_set_animal(self):
        # Test setting the animal of the exhibit
        self.exhibit.set_animal("Snake")
        self.assertEqual(self.exhibit.get_animal(), "Snake")

    def test_get_animal(self):
        # Test getting the animal of the exhibit
        self.assertEqual(self.exhibit.get_animal(), "Giraffe")

    def test_open_exhibit(self):
        # Test opening the exhibit
        self.exhibit.closed_exhibit()   # Ensure exhibit is closed before opening
        self.exhibit.open_exhibit()
        self.assertTrue(self.exhibit.is_exhibit_open())
    def test_closed_exhibit(self):
        # Test closing the exhibit
        self.exhibit.closed_exhibit()
        self.assertFalse(self.exhibit.is_exhibit_open())

    def test_is_exhibit_open(self):
        # Test checking if the exhibit is open
        self.assertTrue(self.exhibit.is_exhibit_open())

if __name__ == '__main__':
    unittest.main()