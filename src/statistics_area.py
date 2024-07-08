from typing import List, Tuple
from collections import Counter
from src.location import Location
from src.area import Exhibit, Area, Entry, Restaurant
from src.utils import check_location_is_within_area
from visited_area_script import determine_visited_area
import math

class StatisticsArea:
    def __init__(self, areas):
        # Initialize with a list of all areas in the zoo
        self.all_areas = areas
        self.visited_sequences = [] # List to store the sequences of areas visited by each visitor

    def add_visitor_path(self, path: List[Tuple[int, int]]):
        # Add a visitor's path, determining the areas visited
        visited_areas = determine_visited_area(path, self.all_areas)
        self.visited_sequences.append(visited_areas)

    def aggregate_visits(self):
        # Count visits for each area, excluding entry area
        aggregated_visits = Counter()
        for sequence in self.visited_sequences:
            filtered_areas = [area for area in sequence if not area == "Entry"]
            aggregated_visits.update(filtered_areas)
        return aggregated_visits

    def most_visited_area(self):
        # Return the name of the most visited area
        aggregated_visits = self.aggregate_visits()
        most_visited_area = aggregated_visits.most_common(1)[0][0]
        return most_visited_area

    def exhibit_visits(self):
        # Count visits for each exhibit, excluding other area
        exhibit_visits = Counter()
        for sequence in self.visited_sequences:
            filtered_areas = [area for area in sequence if area.startswith("Exhibit")]
            exhibit_visits.update(filtered_areas)
        return exhibit_visits

    def most_visited_exhibit(self):
        # Return the name of the most visited exhibit
        exhibit_visits = self.exhibit_visits()
        most_visited_exhibit = exhibit_visits.most_common(1)[0][0]
        return most_visited_exhibit

    def exhibit_revisits(self):
        # Count revisits for each exhibit, excluding other areas
        exhibit_revisits = Counter()
        for sequence in self.visited_sequences:
            # Create a Counter to count the occurrences of each exhibit in the sequence
            exhibit_counts = Counter(area for area in sequence if area.startswith("Exhibit"))
            # Filter out exhibits that are visited only once (no revisits)
            revisited_areas = {area: count for area, count in exhibit_counts.items() if count > 1}
            exhibit_revisits.update(revisited_areas)
        return exhibit_revisits

    def revisited_exhibits(self):
        # Return a list of all revisited exhibits
        exhibit_revisits = self.exhibit_revisits()
        return [exhibit for exhibit, count in exhibit_revisits.items() if count > 1]

    def not_revisited_exhibits(self):
        # Return a list of exhibits not revisited
        exhibit_revisits = self.exhibit_revisits()
        revisited_exhibits = {exhibit for exhibit, count in exhibit_revisits.items() if count > 1}
        return [item.name for item in self.all_areas if isinstance(item, Exhibit) and item.name not in revisited_exhibits]

    def get_all_exhibits(self):
        all_exhibits = []
        for area in self.all_areas:
            if isinstance(area, Exhibit):
                all_exhibits.append(area.name)
        return all_exhibits

    def closest_skipped_exhibits(self):
        exhibit_visits = self.exhibit_visits()
        visited_exhibits = set(exhibit_visits.keys())

        # Get all exhibits as Exhibit objects
        all_exhibits = [area for area in self.all_areas if isinstance(area, Exhibit)]
        all_exhibit_names = {exhibit.name for exhibit in all_exhibits}
        skipped_exhibit_names = all_exhibit_names - visited_exhibits

        # Get skipped exhibit objects
        skipped_exhibits = [exhibit for exhibit in all_exhibits if exhibit.name in skipped_exhibit_names]

        all_skipped_exhibits = []

        for sequence in self.visited_sequences:
            skipped_exhibits_with_distances = []

            for skipped_exhibit in skipped_exhibits:
                min_distance = float('inf')
                for path_loc in sequence:
                    for skipped_loc in skipped_exhibit.geofence:
                        if isinstance(skipped_loc, Location) and isinstance(path_loc, Location):
                            distance = abs(skipped_loc.longitude - path_loc.longitude) + abs(
                                skipped_loc.latitude - path_loc.latitude)
                            if distance < min_distance:
                                min_distance = distance
                skipped_exhibits_with_distances.append((skipped_exhibit, min_distance))

            # Sort skipped exhibits by minimum distance for this path
            skipped_exhibits_with_distances.sort(key=lambda x: x[1])

            # Extract the closest exhibit for this path
            if skipped_exhibits_with_distances:
                closest_skipped_exhibit = skipped_exhibits_with_distances[0][0]
                all_skipped_exhibits.append(closest_skipped_exhibit)

        return all_skipped_exhibits
