import csv
import random

# Generate a 64 by 64 grid filled with zeros
grid = [[0] * 64 for _ in range(64)]

# Randomly select 5 cells to place ones
selected_cells = random.sample(range(64 * 64), 5)

# Place ones in the selected cells
for cell in selected_cells:
    row = cell // 64
    col = cell % 64
    grid[row][col] = 1

# Save the grid to a CSV file
filename = 'report_information.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(grid)

print(f"Grid saved to {filename}")