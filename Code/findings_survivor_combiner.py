import csv

# Specify the paths to the input CSV files
file1_path = '/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Code/survivor.csv'
file2_path = '/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Code/findings.csv'

# Specify the path to the output combined CSV file
output_path = 'survivor_findings_data.csv'

# Read the data from the first CSV file
with open(file1_path, 'r') as file1:
    reader1 = csv.reader(file1)
    data1 = list(reader1)

# Read the data from the second CSV file
with open(file2_path, 'r') as file2:
    reader2 = csv.reader(file2)
    data2 = list(reader2)

# Ensure both files have the same shape (128 by 128)
if len(data1) != 128 or len(data2) != 128:
    raise ValueError("The input CSV files must have a shape of 128 by 128.")

# Combine the values from both files
combined_data = []
for row1, row2 in zip(data1, data2):
    if len(row1) != 128 or len(row2) != 128:
        raise ValueError("The input CSV files must have a shape of 128 by 128.")
    
    combined_row = []
    for value1, value2 in zip(row1, row2):
        if value1 == '1':
            combined_row.append(value1)
        else:
            combined_row.append(value2)
    
    combined_data.append(combined_row)

# Write the combined data to the output CSV file
with open(output_path, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(combined_data)

print(f"Combined data has been written to {output_path}.")