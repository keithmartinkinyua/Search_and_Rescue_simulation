import csv
import random

# Load the map grid from the CSV file
with open('/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Data1/geographical_features.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    map_grid = [[float(value) for value in row] for row in reader]

# Define the feature types and their corresponding values
feature_types = {
    0.1: 'building',
    0.2: 'church',
    0.3: 'library',
    0.4: 'park',
    0.5: 'apartment'
}

# Create a new grid to represent the map with potential survivors
survivor_grid = [[0 for _ in range(len(map_grid[0]))] for _ in range(len(map_grid))]

# Get the positions of the features on the map grid
feature_positions = []
for x in range(len(map_grid)):
    for y in range(len(map_grid[0])):
        feature_value = map_grid[x][y]
        if feature_value in feature_types:
            feature_positions.append((x, y))

# Randomly select 16 feature positions to place survivors
selected_positions = random.sample(feature_positions, 16)

# Place the survivors on the selected positions
for position in selected_positions:
    x, y = position
    survivor_grid[x][y] = 1

# Save the survivor grid to a CSV file
with open('survivor.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(survivor_grid)
    print("Data saved successfully!")