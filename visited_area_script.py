from typing import List, Tuple
from src.location import Location
from src.area import Area, Restaurant, Exhibit, Entry
from src.utils import check_location_is_within_area


def determine_visited_area(path: List[Tuple[int, int]], areas: List[Area]) -> List[str]:
    visited_areas = []  # Use a list to maintain order
    last_visited_area = None  # Track the last visited area to avoid consecutive duplicates

    # Iterate over each coordinate in the path
    for (longitude, latitude) in path:
        location = (longitude, latitude) # Current location as a tuple (longitude, latitude)

        # Iterate over each area in the list of areas
        for area in areas:
            # Create a list of tuples representing the geofence of the area
            geofence = [(loc.get_longitude(), loc.get_latitude()) for loc in area.get_geofence()]

            # Check if the current location is within the geofence of the area
            if check_location_is_within_area(location, geofence):
                # Only add to visited_areas if it's different from the last visited area
                if area.name != last_visited_area:
                    visited_areas.append(area.name)
                    last_visited_area = area.name
                break

    return list(visited_areas)