import unittest
from zoo_map import ZooMap

"""
This file contains test cases for the ZooMap class.
It includes tests for initializing the ZooMap object and for displaying the zoo information.
"""

class TestZooMap(unittest.TestCase):
    def setUp(self):
        # Initialize a ZooMap object
        self.zoo = ZooMap("London Zoo", "United Kingdom", "London", 1_300_000)

    def test_initialization(self):
        # Test if the ZooMap object is initialized correctly with the given attributes
        self.assertEqual(self.zoo.name, "London Zoo")
        self.assertEqual(self.zoo.country, "United Kingdom")
        self.assertEqual(self.zoo.city, "London")
        self.assertEqual(self.zoo.average_visitors_per_year, 1_300_000)

    def test_display_info(self):
        # Test the display_info method for the initialized ZooMap object
        expected_output = (
                "Name of the zoo: London Zoo\n"
                "Country: United Kingdom\n"
                "City: London\n"
                "Average number of visitors per year: 1,300,000\n"
        )
        self.assertEqual(self.zoo.display_info(), expected_output)

    def test_display_info_different_data(self):
        # Test the display_info method for a different ZooMap object
        zoo2 = ZooMap("Jardin Zoologique National de Rabat", "Morocco", "Rabat", 1_000_000)
        expected_output = (
            "Name of the zoo: Jardin Zoologique National de Rabat\n"
            "Country: Morocco\n"
            "City: Rabat\n"
            "Average number of visitors per year: 1,000,000\n"
        )
        self.assertEqual(zoo2.display_info(), expected_output)


if __name__ == '__main__':
    unittest.main()
