import unittest
from collections import Counter
from src.location import Location
from src.area import Area, Restaurant, Exhibit, Entry
from src.utils import check_location_is_within_area
from visited_area_script import determine_visited_area
from src.statistics_area import StatisticsArea

class TestStatisticsArea(unittest.TestCase):
    def setUp(self):
        # Initialize exhibits and restaurant with their geofences
        self.entry = Entry("Entry", [
            Location(0, 0), Location(1, 0), Location(1, 1), Location(0, 1)], True)

        self.exhibit_a = Exhibit("Exhibit A", [
            Location(30, 30), Location(31, 30), Location(31, 31), Location(30, 31)], "Snake", True)

        self.exhibit_b = Exhibit("Exhibit B", [
            Location(40, 40), Location(41, 40), Location(41, 41), Location(40, 41)], "Lion", True)

        self.exhibit_c = Exhibit("Exhibit C", [
            Location(50, 50), Location(51, 50), Location(51, 51), Location(50, 51)], "Giraffe", True)

        self.restaurant = Restaurant("Restaurant", [
            Location(60, 60), Location(61, 60), Location(61, 61), Location(60, 61)], "Takeaway", True)

        self.all_areas = [self.entry, self.exhibit_a, self.exhibit_b, self.exhibit_c, self.restaurant]
        self.stats = StatisticsArea(self.all_areas)

    def test_add_visitor_path(self):
        path = [(0, 0), (30, 30), (40, 40), (50, 50), (60, 60)]
        self.stats.add_visitor_path(path)
        self.assertEqual(len(self.stats.visited_sequences), 1)

    def test_aggregate_visits(self):
        path1 = [(0, 0), (30, 30), (40, 40), (50, 50), (60, 60)]
        path2 = [(0, 0), (40, 40), (30, 30), (50, 50), (60, 60)]
        self.stats.add_visitor_path(path1)
        self.stats.add_visitor_path(path2)
        aggregated_visits = self.stats.aggregate_visits()
        expected = Counter({'Exhibit A': 2,'Exhibit B': 2,'Exhibit C': 2,'Restaurant': 2})
        self.assertEqual(aggregated_visits, expected)

    def test_most_visited_area(self):
        path1 = [(0, 0), (30, 30), (40, 40), (60, 60)]
        path2 = [(0, 0), (50, 50), (60, 60)]
        self.stats.add_visitor_path(path1)
        self.stats.add_visitor_path(path2)
        most_visited_area = self.stats.most_visited_area()
        self.assertEqual(most_visited_area, 'Restaurant')

    def test_most_visited_exhibit(self):
        path1 = [(0, 0), (30, 30), (40, 40)]
        path2 = [(0, 0), (30, 30), (50, 50), (60, 60)]
        self.stats.add_visitor_path(path1)
        self.stats.add_visitor_path(path2)
        most_visited_exhibit = self.stats.most_visited_exhibit()
        self.assertEqual(most_visited_exhibit, 'Exhibit A')

    def test_revisited_exhibits(self):
        path1 = [(0, 0), (30, 30), (40, 40), (30, 30), (60, 60)]
        path2 = [(0, 0), (40, 40), (30, 30), (50, 50), (60, 60), (50, 50)]
        self.stats.add_visitor_path(path1)
        self.stats.add_visitor_path(path2)
        revisited_exhibits = self.stats.revisited_exhibits()
        self.assertEqual(revisited_exhibits, ['Exhibit A', 'Exhibit C'])

    def test_not_revisited_exhibits(self):
        path1 = [(0, 0), (30, 30), (40, 40), (30, 30), (60, 60)]
        path2 = [(0, 0), (40, 40), (30, 30), (50, 50), (60, 60), (50, 50)]
        self.stats.add_visitor_path(path1)
        self.stats.add_visitor_path(path2)
        not_revisited_exhibits = self.stats.not_revisited_exhibits()
        self.assertEqual(not_revisited_exhibits, ['Exhibit B'])

    def test_get_all_exhibits(self):
        all_exhibits = self.stats.get_all_exhibits()
        self.assertEqual(all_exhibits, ["Exhibit A", "Exhibit B", "Exhibit C"])

    def test_closest_skipped_exhibit(self):
        path1 = [(0, 0), (30, 30), (60,60)]
        self.stats.add_visitor_path(path1)
        closest_skipped_exhibits = self.stats.closest_skipped_exhibits()
        self.assertEqual([exhibit.name for exhibit in closest_skipped_exhibits], ['Exhibit B'])


if __name__ == '__main__':
    unittest.main()