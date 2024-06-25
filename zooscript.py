import numpy as np
import matplotlib.pyplot as plt
import random
from src.area import Area, Restaurant, Exhibit, Entry
from src.location import Location

grid_size = 100
num_steps = 1000

def generate_random_walk(grid_size, num_steps):
    # Starts at the center of the grid (50,50)
    start_position = (grid_size // 2, grid_size // 2)
    path = [start_position]

    # possible moves (right, left, up, down)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    current_position = start_position

    for _ in range(num_steps):
        move = random.choice(moves)
        new_position = (current_position[0] + move[0], current_position[1] + move[1])

        # Ensures that the new position is within the grid boundaries
        new_position = (
            max(0, min(grid_size - 1, new_position[0])),
            max(0, min(grid_size - 1, new_position[1]))
        )

        path.append(new_position)
        current_position = new_position

    # Returns to the starting position to complete the cycle
    path.append(start_position)

    return path

def plot_path_and_areas(path, areas, grid_size):
    x, y = zip(*path)

    plt.figure(figsize=(10, 10))

    # Plots the entire path including return to the start
    plt.plot(x, y, marker='o', linestyle='-', color='blue', markersize=3, label='Path')

    # key to highlight the return to the start point
    plt.plot([x[-2], x[-1]], [y[-2], y[-1]], 'r--', linewidth=2, label='Return to Start')

    # key for the starting point
    plt.plot(x[0], y[0], 'go', markersize=10, label='Start/End Point')

    # Plot each area
    for area in areas:
        geofence = [(loc.get_longitude(), loc.get_latitude()) for loc in area.get_geofence()]
        geofence.append(geofence[0])  # Close the loop
        x_area, y_area = zip(*geofence)
        plt.plot(x_area, y_area, marker='o', linestyle='-', markersize=5, label=f'Area: {area.name}')

    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.title('Visitor Path and Zoo Areas')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.legend()
    plt.show()


# Define some sample areas
areas = [
    Entry("Entry", [
        Location(48, 48), Location(52, 48), Location(52, 52), Location(48, 52)], True),
    Exhibit("Giraffe Exhibit", [
        Location(40, 40), Location(45, 40), Location(45, 45), Location(40, 45)],
        "Giraffe", True),
    Exhibit("Snake Exhibit", [
        Location(60, 60), Location(65, 62), Location(63, 68), Location(58, 67), Location(57, 63)],
        "Snake", True),
    Restaurant("La Brasserie", [
        Location(10, 10), Location(20, 10), Location(20, 20), Location(10, 20)],
        "Takeaway")
]


# Generate and plot the random walk path
if __name__ == "__main__":
    path = generate_random_walk(grid_size, num_steps)
    plot_path_and_areas(path, areas, grid_size)
