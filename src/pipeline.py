from utils import check_location_is_within_area
from area import Area
from location import Location
from simulator import generate_random_walk_within_boundary, define_areas, plot_path_with_boundary_and_areas
from typing import List
from src.statistics_area import StatisticsArea

def simulate(areas: List[Area], gridSize: int, noSteps: int, boundaryPath: List[Location]) -> List[Area]:
    """
    Simulates a random walk within a given boundary and tracks visited areas.
    
    :param areas: List of `Area` objects to check for visits.
    :param gridSize: The size of the grid for the random walk.
    :param noSteps: The number of steps for the random walk.
    :param boundaryPath: A list of `Location` objects defining the boundary.
    :return: List of `Area` objects that were visited during the walk.
    """

    # Generate the random walk path

    path = generate_random_walk_within_boundary(gridSize, noSteps, boundaryPath)
    areas = define_areas()

    plot_path_with_boundary_and_areas(path, boundary_path, grid_size, areas)

    print("generated random walk")

    stats_area = StatisticsArea(areas)
    stats_area.add_visitor_path([(loc.get_longitude(), loc.get_latitude()) for loc in path])

    print("statistics:")
    print("Most visited area:", stats_area.most_visited_area())
    print("Most visited exhibit:", stats_area.most_visited_exhibit())
    print("Revisited exhibits:", stats_area.revisited_exhibits())
    print("Not revisited exhibits:", stats_area.not_revisited_exhibits())
    print("All exhibits:", stats_area.get_all_exhibits())
    print("Closest skipped exhibits:", [exhibit.name for exhibit in stats_area.closest_skipped_exhibits()])


print("running")

# Example Usage
boundary_path = [Location(0, 0), Location(0, 80), Location(80, 80), Location(80, 0), Location(60, 0), Location(60, 60), Location(20, 60), Location(20, 0), Location(0, 0)]
grid_size = 100
num_steps = 30000
areas = define_areas()

print("calling simulate")
simulate(areas, grid_size, num_steps, boundary_path)