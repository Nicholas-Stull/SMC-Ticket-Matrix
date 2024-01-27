import csv

# Open the CSV file
with open('example.csv', newline='') as csvfile:
    # Read the CSV file
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Initialize an empty dictionary
    matrix = {}

    # Loop through each row of the CSV file
    for row in csv_reader:
        # Set the first cell of the row as the key
        key = row[0]

        # Set the remaining cells of the row as the values
        values = row[1:]

        # Add the key and values to the dictionary
        matrix[key] = values

# Save the resulting dictionary as a Python file
with open('matrix.py', 'w') as pyfile:
    pyfile.write('matrix = ' + str(matrix))

# Print a confirmation message
print('The resulting dictionary has been saved as a Python file.')
