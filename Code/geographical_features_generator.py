import random
import csv

# Define the grid size
grid_size = (64, 64)

# Define the feature types and their corresponding values
feature_types = {
    'building': 0.1,
    'church': 0.2,
    'library': 0.3,
    'park': 0.4,
    'apartment': 0.5
}

# Define the number of features to be placed
num_features = {
    'building': 5,
    'church': 4,
    'library': 5,
    'park': 10,
    'apartment': 10
}

# Create the grid
grid = [[0.0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]

# Place the features on the grid
for feature_type, num in num_features.items():
    for _ in range(num):
        x = random.randint(0, grid_size[0] - 1)
        y = random.randint(0, grid_size[1] - 1)
        
        # Check if the cell is already occupied by a feature
        if grid[x][y] == 0.0:
            # Place the feature on the grid
            grid[x][y] = feature_types[feature_type]
            
            # Expand the feature to cover multiple cells if needed
            if feature_type == 'park':
                park_size = random.randint(1, 5)
                for i in range(max(0, x - park_size // 2), min(grid_size[0], x + park_size // 2 + 1)):
                    for j in range(max(0, y - park_size // 2), min(grid_size[1], y + park_size // 2 + 1)):
                        grid[i][j] = feature_types[feature_type]
            elif feature_type == 'apartment':
                apartment_size = random.randint(1, 3)
                for i in range(max(0, x - apartment_size // 2), min(grid_size[0], x + apartment_size // 2 + 1)):
                    for j in range(max(0, y - apartment_size // 2), min(grid_size[1], y + apartment_size // 2 + 1)):
                        grid[i][j] = feature_types[feature_type]

# Save the grid to a CSV file
with open('geographical_features.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(grid)
    print("Data has been saved.")