from utils import check_location_is_within_area
from area import Area
from location import Location
from simulator import generate_random_walk_within_boundary
from typing import List

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

    visitedAreas: List[Area] = []
    visitedAreaNames = set()  # To keep track of area names

    for loc in path:
        for area in areas:
            if check_location_is_within_area(loc, area):
                area_name = area.get_name()
                # Avoid adding the same area multiple times
                if area_name not in visitedAreaNames:
                    visitedAreas.append(area)
                    visitedAreaNames.add(area_name)

    return visitedAreas
