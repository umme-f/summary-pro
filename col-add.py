import os
import glob
import pandas as pd

# Set the path to the folder containing CSV files
folder_path = r'C:\Users\Ariake\Desktop\20240304\FL-FOLDER\FL\fl-csv'

# Define the three patterns to match CSV files
file_patterns = ['*fl-combine-cpu-col-col-d.csv', 
                 '*fl-combine-mem-col-col-d.csv', 
                 '*fl-combine-net-col-col-d.csv']

# Column to be added to each CSV file
new_column_name = 'server'
new_column_value = 'FL'  # You can adjust this value as needed

# Iterate through each pattern
for pattern in file_patterns:
    # Use glob to get a list of CSV files with the specified pattern
    csv_files = glob.glob(os.path.join(folder_path, pattern))

    # Check if there are any CSV files for the current pattern
    if csv_files:
        # Iterate through each CSV file
        for file in csv_files:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file, encoding_errors='ignore')

            # Add the new column with the specified value
            df[new_column_name] = new_column_value

            # Save the updated DataFrame back to the CSV file
            df.to_csv(file, index=False)
            
    else:
        print(f"No CSV files found with pattern '{pattern}' in the directory.")
