import tkinter as tk
from tkinter import simpledialog
import heapq
import random
import time
import csv
import os
import numpy as np



# Define the cost map with random values between 0 and 50
base_dir='/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Code'
static_cost_path=os.path.join(base_dir, "amalgamated_cost_map1.csv")
cost_map = np.genfromtxt(static_cost_path, delimiter=",")


# m survivor table 
test_data_path=os.path.join(base_dir, "test_map.csv")
survivor_table = np.genfromtxt(test_data_path, delimiter=",")


survivor_count = 0
while survivor_count < 100:
    x = random.randint(0, 127)
    y = random.randint(0, 127)
    if survivor_table[y][x] == 0:
        survivor_table[y][x] = 1
        survivor_count += 1

# Create a list of all cells with their cost values
cells_with_costs = [(cost_map[y][x], (x, y)) for x in range(128) for y in range(128)]

# Sort the list in descending order based on the cost values
cells_with_costs.sort(reverse=True)

# Define the A* algorithm
def astar(start, end):
    # Initialize the open set and closed set
    open_set = []
    closed_set = set()

    # Add the start node to the open set with its negated cost for max-heap
    heapq.heappush(open_set, (-cost_map[start[1]][start[0]], start))

    # Initialize the g_score and parent dictionaries
    g_score = {start: 0}
    parent = {start: None}

    while open_set:
        # Pop the node with the minimum cost from the open set
        current = heapq.heappop(open_set)[1]

        # Check if the current node is the destination
        if current == end:
            # Reconstruct the path from the parent dictionary
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return the reversed path

        # Add the current node to the closed set
        closed_set.add(current)

        # Find the neighbors of the current node
        neighbors = get_neighbors(current)

        # Process each neighbor
        for neighbor in neighbors:
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + cost_map[neighbor[1]][neighbor[0]]

            # Check if the neighbor needs to be updated
            if neighbor not in [node[1] for node in open_set] or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                parent[neighbor] = current
                heapq.heappush(open_set, (-cost_map[neighbor[1]][neighbor[0]], neighbor))  # Negating the cost for max-heap

    return []  # No path found

def get_neighbors(node):
    # Get the valid neighbors of the given node
    neighbors = []
    x, y = node
    if x > 0:
        neighbors.append((x - 1, y))
    if x < 127:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < 127:
        neighbors.append((x, y + 1))
    return neighbors

# Define the Tkinter window and canvas
root = tk.Tk()
root.title("Robot Movement Simulation")
canvas = tk.Canvas(root, width=1024, height=1024)
canvas.pack()

# Draw the grid
cell_size = 8
for i in range(128):
    for j in range(128):
        x1 = j * cell_size
        y1 = i * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

def simulate_robot():
    global start_x, start_y

    # Mark the start position on the canvas
    start_center_x = start_x * cell_size + cell_size // 2
    start_center_y = start_y * cell_size + cell_size // 2
    canvas.create_oval(start_center_x - 4, start_center_y - 4, start_center_x + 4, start_center_y + 4, fill="green", outline="")

    # Start the timer and initialize the cell count
    start_time = time.time()
    total_cells_traveled = 0

    # Open the CSV file for appending
    with open('amalgamated_cost_map_on_test_map_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row if the file is empty
        if file.tell() == 0:
            writer.writerow(['Cell Location', 'Number of Cells Traveled', 'Time Taken (seconds)'])

        # Traverse the cost map in descending order of cost values
        for cost, (end_x, end_y) in cells_with_costs:
            # Mark the destination position on the canvas
            end_center_x = end_x * cell_size + cell_size // 2
            end_center_y = end_y * cell_size + cell_size // 2
            canvas.create_oval(end_center_x - 4, end_center_y - 4, end_center_x + 4, end_center_y + 4, fill="red", outline="")

            # Find the path using the A* algorithm
            path = astar((start_x, start_y), (end_x, end_y))

            # Draw the path and simulate robot movement on the canvas
            for i, cell in enumerate(path):
                x, y = cell
                center_x = x * cell_size + cell_size // 2
                center_y = y * cell_size + cell_size // 2
                canvas.create_oval(center_x - 4, center_y - 4, center_x + 4, center_y + 4, fill="blue", outline="")
                canvas.update()
                canvas.after(100)  # Delay for animation

            # Update the total cells traveled
            total_cells_traveled += len(path)

            # Check if the destination cell contains a survivor
            if survivor_table[end_y][end_x] == 1:
                current_time = time.time() - start_time
                print(f"Survivor found at cell ({end_x}, {end_y}) after {current_time:.2f} seconds and {total_cells_traveled} cells traveled")

                # Write the survivor data to the CSV file
                writer.writerow([f"({end_x}, {end_y})", total_cells_traveled, f"{current_time:.2f}"])
                file.flush()  # Flush the data to the file

            # Update the start position for the next iteration
            start_x, start_y = end_x, end_y

    # Print the overall time taken and total cells traveled for the robot's traversal
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Robot's traversal completed. Overall time taken: {elapsed_time:.2f} seconds, Total cells traveled: {total_cells_traveled}")

# Get the initial start coordinates from the user
start_coords = simpledialog.askstring("Start Coordinates", "Enter the start coordinates (x,y):")
start_x, start_y = map(int, start_coords.split(","))

# Start the simulation
simulate_robot()

root.mainloop()