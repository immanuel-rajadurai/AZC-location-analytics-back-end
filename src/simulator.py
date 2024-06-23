from typing import List, Tuple
import random
import matplotlib.pyplot as plt
from location import Location
from area import Area


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


# plots path within a given boundary
def plot_path_with_boundary(path: List[Location], boundary_path: List[Location], grid_size: int):
    x, y = zip(*[(loc.get_longitude(), loc.get_latitude()) for loc in path])
    bx, by = zip(*[(loc.get_longitude(), loc.get_latitude()) for loc in boundary_path])

    plt.figure(figsize=(10, 10))

    plt.plot(x, y, marker='o', linestyle='-', color='blue', markersize=3, label='Path')
    plt.plot([x[-2], x[-1]], [y[-2], y[-1]], 'r--', linewidth=2, label='Return to Start')
    plt.plot(x[0], y[0], 'go', markersize=10, label='Start/End Point')
    plt.plot(bx, by, 'k-', linewidth=2, label='Boundary Path')

    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.title('Random Zoo Walk Path Within Boundary')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.legend()
    plt.show()


# Example Usage
boundary_path = [Location(0, 0), Location(0, 80), Location(80, 80), Location(80, 0), Location(60, 0), Location(60, 60), Location(20, 60), Location(20, 0), Location(0, 0)]
grid_size = 100
num_steps = 30000

path = generate_random_walk_within_boundary(grid_size, num_steps, boundary_path)
plot_path_with_boundary(path, boundary_path, grid_size)
