# This line imports the CSV file.
import csv

# These two lines specify the input and output CSV file names.
input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'

# These three lines read the CSV file.
with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# These two lines define the new status column and the pending default value for each row.
new_column_name = 'Status'
default_value = 'Pending'

# This line adds a new column 'Status' to the header.
header = data[0] + [new_column_name]

# This line adds a new 'Pending' column to each row.
rows = [row + [default_value] for row in data[1:]]

# These four lines write the new modified data to the new 'security_incidents_modified.csv' file.
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

# The last line prints a statement saying "Modified data saved to 'security_incidents_modified.csv'."
print(f"Modified data saved to '{output_file}'")
