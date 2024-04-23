import random
import csv

def generate_road_network(rows, cols, road_density, impassable_density, impassable_region_size):
    grid = [[1] * cols for _ in range(rows)]

    # Generate impassable regions
    num_impassable_regions = int((rows * cols) * impassable_density)
    for _ in range(num_impassable_regions):
        start_row = random.randint(0, rows - impassable_region_size)
        start_col = random.randint(0, cols - impassable_region_size)
        for i in range(start_row, start_row + impassable_region_size):
            for j in range(start_col, start_col + impassable_region_size):
                grid[i][j] = 0

    # Ensure consistency of the road network
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                # Check neighboring cells
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for ni, nj in neighbors:
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        # Connect neighboring road cells
                        grid[ni][nj] = 1

    return grid

# Parameters
rows = 64
cols = 64
road_density = 0.8
impassable_density = 0.1
impassable_region_size = 3

# Generate the road network
road_network = generate_road_network(rows, cols, road_density, impassable_density, impassable_region_size)

# Save the road network to a CSV file
filename = 'road_network.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(road_network)

print(f"Road network saved to {filename}")