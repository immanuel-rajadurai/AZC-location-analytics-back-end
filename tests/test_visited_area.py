import unittest
from src.location import Location
from src.area import Area, Restaurant, Exhibit, Entry
#from zooscript import generate_random_walk_within_boundary
from visited_area_script import determine_visited_area

class TestDetermineVisitedAreas(unittest.TestCase):
    # Initialize exhibits and restaurant with their geofences
    def setUp(self):
        self.entry1 = Entry("Entry", [
            Location(48, 48), Location(52, 48), Location(52, 52), Location(48, 52)], True)

        self.exhibit1 = Exhibit("Giraffe Exhibit", [
            Location(40, 40), Location(45, 40), Location(45, 45), Location(40, 45)],
            "Giraffe", True)

        self.exhibit2 = Exhibit("Snake Exhibit", [
            Location(60, 60), Location(65, 62), Location(63, 68), Location(58, 67), Location(57, 63)],
            "Snake", True)

        self.restaurant = Restaurant("La Brasserie", [
            Location(10, 10), Location(20, 10), Location(20, 20), Location(10, 20)],
            "Takeaway")

        self.areas = [self.entry1, self.exhibit1, self.exhibit2, self.restaurant]

    def test_empty_path(self):
        # Test an empty path
        path = []
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, [])

    def test_path_visits_no_area(self):
        # Test a path that doesn't enter any area
        path = [(0, 0), (1, 1), (2, 2)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, [])

    def test_path_visits_one_area(self):
        # Test a path that enters only one area
        path = [(50, 50),(52, 52)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, ["Entry"])

    def test_path_visits_multiple_areas(self):
        # Test a path that enters multiple areas
        path = [(0, 0), (10, 10), (15, 15), (40, 40), (45, 45), (63, 64), (64, 65)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertIn("La Brasserie", visited_areas)
        self.assertIn("Giraffe Exhibit", visited_areas)
        self.assertIn("Snake Exhibit", visited_areas)

    def test_path_visits_area_multiple_times(self):
        # Test a path that visits an area multiple times
        path = [(10, 10), (15, 15), (10, 10), (15, 15)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, ["La Brasserie"])

    def test_path_visits_all_areas_reverse(self):
        # Test a path that visits all areas in reverse order
        path = [(63, 64), (64, 65), (45, 45), (40, 40), (15, 15), (10, 10)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, ["Snake Exhibit", "Giraffe Exhibit", "La Brasserie"])

    def test_path_visits_areas_twice(self):
        # Test a path that visits some areas twice
        path = [(63, 64), (64, 65), (45, 45), (40, 40), (15, 15), (10, 10), (45,45), (40, 40)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, ["Snake Exhibit", "Giraffe Exhibit", "La Brasserie", "Giraffe Exhibit"])

    def test_repeated_path_visits_one_area(self):
        # Repeat the test_path_visits_one_area multiple times
        path = [(50, 50), (52, 52)]
        for i in range(100):  # Repeat 100 times
            with self.subTest(i=i):
                visited_areas = determine_visited_area(path, self.areas)
                self.assertEqual(visited_areas, ["Entry"])

    def test_repeated_path_visits_area_multiple_times(self):
        # Repeat the test_path_visits_area_multiple_times multiple times
        path = [(10, 10), (15, 15), (10, 10), (15, 15)]
        for i in range(100):  # Repeat 100 times
            with self.subTest(i=i):
                visited_areas = determine_visited_area(path, self.areas)
                self.assertEqual(visited_areas, ["La Brasserie"])

    def test_path_at_area_boundary(self):
        # Test a path that enters a point at the boundary of an area
        path = [(48, 48), (52, 48)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, ["Entry"])

    def test_path_outside_all_areas(self):
        # Test a path that is completely outside all areas
        path = [(0, 0), (5, 5), (0, 5)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, [])

    def test_path_along_area_boundary(self):
        # Test a path that follows along the boundary of an area
        path = [(48, 48), (49, 48), (50, 48), (51, 48), (52, 48)]
        visited_areas = determine_visited_area(path, self.areas)
        self.assertEqual(visited_areas, ["Entry"])


if __name__ == '__main__':
    unittest.main()