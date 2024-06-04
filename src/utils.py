from typing import List, Tuple
from scipy.spatial import ConvexHull

"""
Determines whether a location (in form of a tuple coordinates (longitude, latitude)) 
is within an area (a polygon given in the form of a list of locations (tuples))
Computes the Convex hull to ensure that the area polygon forms a closed perimeter, where no edges intersect
Runs within O(n) time, where n is the number of edges
"""

def check_location_is_on_edge(point: Tuple[int, int], edge: Tuple[Tuple[int, int]]):
    (x,y) = point
    (x1, y1), (x2, y2) = edge

    #Check if the point is co-linear with the edge
    if (x2-x1) * (y-y1) != (y2-y1) * (x-x1):
        return False
    
    #Check if the point is between the points
    if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1,y2):
        return True
    else:
        return False


def check_location_is_within_area(location: Tuple[int, int], area:List[Tuple[int,int]]):
    xp = location[0]
    yp = location[1]


    #Calculate the Convex hull to ensure a complete perimeter
    hull = ConvexHull(area)
    vertices = [area[vertex] for vertex in hull.vertices]
    vertices.append(vertices[0])
    edges = [(vertices[i], vertices[i+1]) for i in range(len(vertices)-1)]

    counter = 0

    for edge in edges:
        #If the point is on the edge, it is immediately in the area
        if (check_location_is_on_edge(location, edge)):
            return True
        
        (x1, y1), (x2, y2) = edge

        #Algorithm to check if the point intersects, the edge, increments counter if it does
        if (yp < y1) != (yp < y2) and xp < x1 +((yp-y1)/(y2-y1)) * (x2-x1):
            counter += 1
    
    return counter%2 == 1
