from typing import List, Tuple
from scipy.spatial import ConvexHull
from src.location import Location


"""
Determines whether a location (in form of a tuple coordinates (longitude, latitude)) 
is within an area (a polygon given in the form of a list of locations (tuples))
Computes the Convex hull to ensure that the area polygon forms a closed perimeter, where no edges intersect
Runs within O(n) time, where n is the number of edges
"""

def check_location_is_on_edge(point: Location, edge: Tuple[Location, Location]) -> bool:
    x, y = point.get_longitude(), point.get_latitude()
    p1, p2 = edge
    x1, y1 = p1.get_longitude(), p1.get_latitude()
    x2, y2 = p2.get_longitude(), p2.get_latitude()

    #Check if the point is co-linear with the edge
    if (x2-x1) * (y-y1) != (y2-y1) * (x-x1):
        return False
    
    #Check if the point is between the points
    if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1,y2):
        return True 
    else:
        return False


def check_location_is_within_area(location: Tuple[float, float], area: List[Tuple[float, float]]) -> bool:
    xp, yp = location

    points = area

    # Calculate the Convex hull to ensure a complete perimeter
    hull = ConvexHull(points)

    vertices = [points[vertex] for vertex in hull.vertices]
    vertices.append(vertices[0])
    edges = [(vertices[i], vertices[i+1]) for i in range(len(vertices)-1)]

    counter = 0

    for edge in edges:
        (x1, y1), (x2, y2) = edge

        # Algorithm to check if the point intersects the edge, increments counter if it does
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp - y1) / (y2 - y1)) * (x2 - x1):
            counter += 1

    return counter % 2 == 1
