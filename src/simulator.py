from typing import List, Tuple
import random
import matplotlib.pyplot as plt
from src.location import Location
from src.area import Exhibit, Area, Entry, Restaurant


# determines whether path point is inside a given polygon boundary
def is_point_inside_polygon(point: Tuple[float, float], polygon: List[Tuple[float, float]]) -> bool:
    x, y = point
    n = len(polygon)
    inside = False

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside


# generates random walk within a given boundary path
def generate_random_walk_within_boundary(grid_size: int, num_steps: int, boundary_path: List[Location]) -> List[Location]:
    start_position = (boundary_path[0].get_longitude(), boundary_path[0].get_latitude())
    path = [start_position]

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    current_position = start_position

    for step in range(num_steps):
        valid_move_found = False
        while not valid_move_found:
            move = random.choice(moves)
            new_position = (current_position[0] + move[0], current_position[1] + move[1])

            new_position = (
                max(0, min(grid_size - 1, new_position[0])),
                max(0, min(grid_size - 1, new_position[1]))
            )

            if is_point_inside_polygon(new_position, [(loc.get_longitude(), loc.get_latitude()) for loc in boundary_path]):
                valid_move_found = True
                path.append(new_position)
                current_position = new_position

    path.append(start_position)
    return [Location(lon, lat) for lon, lat in path]

# Define the areas within the zoo
def define_areas() -> List[Area]:
    entry = Entry("Entry", [
        Location(0, 0), Location(0, 5), Location(5, 5), Location(5, 0)], True)
    exhibit_a = Exhibit("Exhibit A", [
        Location(10, 30), Location(10, 40), Location(20, 40), Location(20, 30)], "Snake", True)
    exhibit_b = Exhibit("Exhibit B", [
        Location(0, 70), Location(0, 80), Location(10, 80), Location(10, 70)], "Lion", True)
    exhibit_c = Exhibit("Exhibit C", [
        Location(60, 50), Location(60, 60), Location(70, 60), Location(70, 50)], "Giraffe", True)
    restaurant = Restaurant("Restaurant", [
        Location(30, 70), Location(30, 80), Location(50, 80), Location(50, 70)], "Takeaway", True)

    areas = [entry, exhibit_a, exhibit_b, exhibit_c, restaurant]
    return areas

# Assign colors to exhibits for visualization
def assign_colors(areas: List[Area]) -> dict:
    colors = ["#FF69B4", "#1E90FF", "#FFA500"]
    random.shuffle(colors)
    color_dict = {}
    for area in areas:
        if isinstance(area, Exhibit):
            color_dict[area.name] = colors.pop()
    return color_dict

# plots path within a given boundary
def plot_path_with_boundary_and_areas(path: List[Location], boundary_path: List[Location], grid_size: int, areas: List[Area]):
    plt.figure(figsize=(12, 10))

    x, y = zip(*[(loc.get_longitude(), loc.get_latitude()) for loc in path])
    bx, by = zip(*[(loc.get_longitude(), loc.get_latitude()) for loc in boundary_path])

    plt.plot(x, y, marker='o', linestyle='-', color='gray', markersize=2, label='Path', alpha=0.3)
    plt.plot([x[-2], x[-1]], [y[-2], y[-1]], linewidth=2,color='purple', label='Return to Start', alpha=0.3)
    plt.plot(x[0], y[0], 'go', markersize=10, label='Start/End Point')
    plt.plot(bx, by, 'k-', linewidth=2, label='Boundary Path')

    exhibit_colors = assign_colors(areas)

    area_colors = {
        "Entry": "darkgreen",
        "Restaurant": "red"
    }

    # Plot each area with its respective color
    for area in areas:
        geofence = [(loc.get_longitude(), loc.get_latitude()) for loc in area.get_geofence()]
        geofence.append(geofence[0])
        x_area, y_area = zip(*geofence)
        area_type = type(area).__name__
        if isinstance(area, Exhibit):
            color = exhibit_colors[area.name]
        else:
            color = area_colors.get(type(area).__name__, "black")
        plt.fill(x_area, y_area, color=color, alpha=1)
        plt.plot(x_area, y_area, marker='o', linestyle='-', markersize=3, color=color, label=f'Area: {area.name}')

    # Configure plot limits and labels
    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.title('Visitor Path and Zoo Areas')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.subplots_adjust(right=0.75)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.show()





