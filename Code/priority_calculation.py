import csv

# Initialize an empty result grid
result_grid = [[0] * 64 for _ in range(64)]

# Load the CSV files
survivor_grid = []
report_grid = []
findings_grid = []

with open('/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Data1/survivor.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    survivor_grid = [[int(value) for value in row] for row in reader]

with open('/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Data1/report_information.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    report_grid = [[int(value) for value in row] for row in reader]

with open('/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Data1/findings.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    findings_grid = [[float(value) for value in row] for row in reader]


# Iterate over each cell in the grid
for i in range(64):
    for j in range(64):
        if survivor_grid[i][j] == 1:
            result_grid[i][j] = 1  
        elif survivor_grid[i][j] == 0 and report_grid[i][j] == 1:
            result_grid[i][j] = 0.6 * report_grid[i][j] + 0.3 * survivor_grid[i][j] + 0.1 * findings_grid[i][j] 
        else:
            result_grid[i][j] = 0.2 * report_grid[i][j] + 0.4 * survivor_grid[i][j] + 0.4 * findings_grid[i][j]

# Save the result grid to a new CSV file
with open('priority.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(result_grid)

print("Result saved to 'priority.csv'")