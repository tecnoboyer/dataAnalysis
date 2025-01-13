import os
import pandas as pd

# Define the directory containing the .csv files
directory = r"C:\Users\technoboyer\Documents\Cuentas"

# Define the correct column names (assuming all files should have these 5 columns)
expected_columns = ["Column1", "Column2", "Column3", "Column4", "Column5"]

# List to hold DataFrames
dataframes = []

# Iterate through all files in the directory
for file in os.listdir(directory):
    if file.endswith(".csv"):
        file_path = os.path.join(directory, file)
        try:
            # Read the .csv file, enforce correct column names, and skip problematic rows
            df = pd.read_csv(file_path, header=None, names=expected_columns)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")

# Merge all DataFrames into a single DataFrame
if dataframes:
    consolidated_df = pd.concat(dataframes, ignore_index=True)
    
    # Save the consolidated DataFrame to a .csv file
    output_file = os.path.join(directory, "consolidated.csv")
    consolidated_df.to_csv(output_file, index=False)
    print(f"Consolidated file saved as: {output_file}")
else:
    print("No .csv files found in the directory.")
