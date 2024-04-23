import csv
import random

# Load the survivor grid from the CSV file
with open('survivor_grid.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    survivor_grid = [[int(value) for value in row] for row in reader]

# Define the findings types and their corresponding values
findings_types = {
    'communication_device': 0.1,
    'personal_belongings': 0.2,
    'attire': 0.3
}

# Define the number of findings to be placed
total_findings = 100

# Create a new grid to represent the combined map
combined_grid = [[0.0 for _ in range(len(survivor_grid[0]))] for _ in range(len(survivor_grid))]

# Copy the survivor grid to the combined grid
for x in range(len(survivor_grid)):
    for y in range(len(survivor_grid[0])):
        combined_grid[x][y] = survivor_grid[x][y]

# Place the findings on the grid
for _ in range(total_findings):
    x = random.randint(0, len(survivor_grid) - 1)
    y = random.randint(0, len(survivor_grid[0]) - 1)
    
    # Check if the cell is already occupied by a survivor
    if combined_grid[x][y] == 0:
        # Randomly choose a finding type
        finding_type = random.choice(list(findings_types.keys()))
        
        # Place the finding on the grid
        combined_grid[x][y] = findings_types[finding_type]
        
        # Check the surrounding cells and place findings randomly
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(survivor_grid) and 0 <= ny < len(survivor_grid[0]) and combined_grid[nx][ny] == 0:
                    finding_type = random.choice(list(findings_types.keys()))
                    combined_grid[nx][ny] = findings_types[finding_type]

# Save the combined grid to a CSV file
with open('test_map.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(combined_grid)
    print("Data successfully saved!")