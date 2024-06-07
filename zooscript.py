import numpy as np
import matplotlib.pyplot as plt
import random

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

def plot_path(path, grid_size):
    x, y = zip(*path)

    plt.figure(figsize=(10, 10))

    # Plots the entire path including return to the start
    plt.plot(x, y, marker='o', linestyle='-', color='blue', markersize=3, label='Path')

    # key to highlight the return to the start point
    plt.plot([x[-2], x[-1]], [y[-2], y[-1]], 'r--', linewidth=2, label='Return to Start')

    # key for the starting point
    plt.plot(x[0], y[0], 'go', markersize=10, label='Start/End Point')

    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.title('Random Zoo Walk Path')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.legend()
    plt.show()


# Generate and plot the random walk path
path = generate_random_walk(grid_size, num_steps)
plot_path(path, grid_size)
