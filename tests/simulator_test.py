from simulator import Location,Area
from area import Exhibit,Restaurant
import unittest

class TestLocation(unittest.TestCase):

    def test_location_initialization(self):
        loc = Location(10.0, 20.0)
        self.assertEqual(loc.get_longitude(), 10.0)
        self.assertEqual(loc.get_latitude(), 20.0)

    def test_set_longitude(self):
        loc = Location(10.0, 20.0)
        loc.set_longitude(15.0)
        self.assertEqual(loc.get_longitude(), 15.0)

    def test_set_latitude(self):
        loc = Location(10.0, 20.0)
        loc.set_latitude(25.0)
        self.assertEqual(loc.get_latitude(), 25.0)

class TestArea(unittest.TestCase):

    def test_area_initialization(self):
        loc1 = Location(10.0, 20.0)
        loc2 = Location(15.0, 25.0)
        area = Area("TestArea", [loc1, loc2])
        self.assertEqual(area.name, "Zoo1")
        self.assertEqual(area.get_geofence(), [loc1, loc2])

    def test_add_location(self):
        loc1 = Location(10.0, 20.0)
        area = Area("TestArea", [loc1])
        loc2 = Location(15.0, 25.0)
        area.add_location(loc2)
        self.assertIn(loc2, area.get_geofence())

    def test_remove_location(self):
        loc1 = Location(10.0, 20.0)
        loc2 = Location(15.0, 25.0)
        area = Area("TestArea", [loc1, loc2])
        area.remove_location(loc2)
        self.assertNotIn(loc2, area.get_geofence())

class TestRestaurant(unittest.TestCase):

    def test_restaurant_initialization(self):
        loc1 = Location(10.0, 20.0)
        loc2 = Location(15.0, 25.0)
        restaurant = Restaurant("TestRestaurant", [loc1, loc2], "Cafe")
        self.assertEqual(restaurant.name, "TestRestaurant")
        self.assertEqual(restaurant.get_restaurant_type(), "Cafe")
        self.assertEqual(restaurant.get_menu(), [])

    def test_add_menu_item(self):
        loc1 = Location(10.0, 20.0)
        restaurant = Restaurant("TestRestaurant", [loc1], "Cafe")
        restaurant.add_menu_item("Coffee")
        self.assertIn("Coffee", restaurant.get_menu())

class TestExhibit(unittest.TestCase):

    def test_exhibit_initialization(self):
        loc1 = Location(10.0, 20.0)
        loc2 = Location(15.0, 25.0)
        exhibit = Exhibit("TestExhibit", [loc1, loc2], "Lion", True)
        self.assertEqual(exhibit.name, "TestExhibit")
        self.assertEqual(exhibit.get_animal(), "Lion")
        self.assertTrue(exhibit.is_exhibit_open())

    def test_open_close_exhibit(self):
        loc1 = Location(10.0, 20.0)
        exhibit = Exhibit("TestExhibit", [loc1], "Lion", False)
        exhibit.open_exhibit()
        self.assertTrue(exhibit.is_exhibit_open())
        exhibit.close_exhibit()
        self.assertFalse(exhibit.is_exhibit_open())

if __name__ == '__main__':
    unittest.main()
