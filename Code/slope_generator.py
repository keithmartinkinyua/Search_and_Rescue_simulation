import csv

# Create a 64 by 64 grid with all cells containing 1
grid = [[1] * 64 for _ in range(64)]

# Save the grid to a CSV file
filename = 'slope.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(grid)

print(f"Grid saved to {filename}")