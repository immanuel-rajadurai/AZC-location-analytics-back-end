import numpy as np
import matplotlib.pyplot as plt
import random


grid_size = 100
num_steps = 3000


# checks to see if path point is within the boundary
def is_point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def generate_random_walk_within_boundary(grid_size, num_steps, boundary_path):
    # The start position is the first point of the boundary path
    start_position = boundary_path[0]
    path = [start_position]

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    current_position = start_position

    print("Starting random walk generation...")

    for step in range(num_steps):
        valid_move_found = False
        while not valid_move_found:
            move = random.choice(moves)
            new_position = (current_position[0] + move[0], current_position[1] + move[1])

            new_position = (
                max(0, min(grid_size - 1, new_position[0])),
                max(0, min(grid_size - 1, new_position[1]))
            )

            if is_point_in_polygon(new_position, boundary_path):
                valid_move_found = True
                path.append(new_position)
                current_position = new_position

        if step % 100 == 0:
            print(f"Step {step} complete. Current position: {current_position}")

    path.append(start_position)
    print("Random walk generation complete.")
    return path


# plots the path within the given boundary
def plot_path_with_boundary(path, boundary_path, grid_size):
    x, y = zip(*path)
    bx, by = zip(*boundary_path)

    plt.figure(figsize=(10, 10))

    plt.plot(x, y, marker='o', linestyle='-', color='blue', markersize=3, label='Path')
    plt.plot([x[-2], x[-1]], [y[-2], y[-1]], 'r--', linewidth=2, label='Return to Start')
    plt.plot(x[0], y[0], 'go', markersize=10, label='Start/End Point')
    plt.plot(bx, by, 'k-', linewidth=2, label='Boundary Path')

    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    plt.title('Random Zoo Walk Path within Custom Boundary')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.legend()
    plt.show()


# allows the user to enter a custom boundary by inputting coordinates
def get_user_defined_boundary():
    print("Enter the boundary path as a series of points (x, y).")
    print("Enter 'done' when you have finished inputting points.")
    boundary = []
    while True:
        user_input = input("Enter point (x, y) or 'done': ")
        if user_input.lower() == 'done':
            break
        try:
            x, y = map(int, user_input.split(','))
            boundary.append((x, y))
        except ValueError:
            print("Invalid input. Please enter the point in the format 'x, y'.")

    if len(boundary) < 3:
        print("A valid boundary requires at least three points.")
        return get_user_defined_boundary()

    if boundary[0] != boundary[-1]:
        boundary.append(boundary[0])

    return boundary


# Gets custom boundary path from the user
boundary_path = get_user_defined_boundary()

# Generates and plots the random walk path within the custom boundary
path = generate_random_walk_within_boundary(grid_size, num_steps, boundary_path)

# message to confirm path generation
print("Random walk path generation complete. Path length:", len(path))
plot_path_with_boundary(path, boundary_path, grid_size)
