import numpy as np
import csv

# Specify the path to the input .npy file
input_file = "/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Code/amalgamated_cost_map.npy"

# Specify the path to the output CSV file
output_file = "/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Code/amalgamated_cost_map1.csv"

# Load the .npy file
data = np.load(input_file)

# Reshape the data to (128, 128)
data_reshaped = data.reshape(128, 128)

# Open the output file in write mode
with open(output_file, "w", newline="") as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write each row of the reshaped data to the CSV file
    for row in data_reshaped:
        writer.writerow(row)

print("Data saved as CSV successfully.")