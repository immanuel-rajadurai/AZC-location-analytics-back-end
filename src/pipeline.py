from utils import check_location_is_within_area
from src.area import Exhibit, Area, Entry, Restaurant
from location import Location
from simulator import generate_random_walk_within_boundary, define_areas, plot_path_with_boundary_and_areas
from typing import List
from src.statistics_area import StatisticsArea
from recurrentNeuralNetwork import loadRNN, predictNextArea
import tensorflow as tf

def simulate(areas, gridSize: int, noSteps: int, boundaryPath: List[Location], model) -> List[Area]:
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

    # Plot the generated path along with the boundary and areas
    plot_path_with_boundary_and_areas(path, boundary_path, grid_size, areas)

    # Initialize the StatisticsArea class with the given areas
    stats_area = StatisticsArea(areas)

    # Convert path to tuples of (longitude, latitude) and add it to stats_area
    stats_area.add_visitor_path([(loc.get_longitude(), loc.get_latitude()) for loc in path])

    # Print statistics about the walk and visited areas
    print("Statistics:")
    print(" - Most visited area:", stats_area.most_visited_area())
    print(" - All exhibits:", stats_area.get_all_exhibits())
    print(" - Most visited exhibit:", stats_area.most_visited_exhibit())
    print(" - Revisited exhibits:", stats_area.revisited_exhibits())
    print(" - Not revisited exhibits:", stats_area.not_revisited_exhibits())
    print(" - Closest skipped exhibits:", [exhibit.name for exhibit in stats_area.closest_skipped_exhibits()])
    print(" - The next area the user will visit will be: " + predictNextArea(path, model))


# Example Usage
boundary_path = [Location(0, 0), Location(0, 80), Location(80, 80), Location(80, 0), Location(60, 0), Location(60, 60), Location(20, 60), Location(20, 0), Location(0, 0)]
grid_size = 100
num_steps = 30000
model = tf.keras.models.load_model('model.h5')
areas = define_areas()
simulate(areas, grid_size, num_steps, boundary_path)