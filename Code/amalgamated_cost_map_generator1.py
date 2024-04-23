import csv

# Initialize an empty result grid
result_grid = [[0] * 64 for _ in range(64)]

# Load the CSV files
static_cost_grid = []
priority_grid = []

try:
    with open('/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Data1/static_cost_map.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        static_cost_grid = [[float(value) for value in row] for row in reader]
except FileNotFoundError:
    print("File 'static_cost_map.csv' not found.")
    exit(1)

try:
    with open('/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Data1/priority.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        priority_grid = [[float(value) for value in row] for row in reader]
except FileNotFoundError:
    print("File 'priority.csv' not found.")
    exit(1)

# Check if the dimensions of static_cost_grid and priority_grid are the same
if len(static_cost_grid) != len(priority_grid) or len(static_cost_grid[0]) != len(priority_grid[0]):
    print("Error: The dimensions of 'static_cost_map.csv' and 'priority.csv' do not match.")
    exit(1)

# Iterate over each cell in the grid
for i in range(len(static_cost_grid)):
    for j in range(len(static_cost_grid[0])):
        if priority_grid[i][j] != 0:
            result_grid[i][j] = static_cost_grid[i][j] / priority_grid[i][j]
        else:
            #result_grid[i][j] = static_cost_grid[i][j]
            result_grid[i][j] = 0

# Save the result grid to a new CSV file
try:
    with open('amalgamated_cost_map.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result_grid)
    print("Result saved to 'amalgamated_cost_map.csv'")
except IOError:
    print("Error occurred while saving the result to 'amalgamated_cost_map.csv'.")
    exit(1)