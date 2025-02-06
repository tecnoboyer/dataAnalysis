import pandas as pd
import os
from datetime import datetime

# Set your OpenAI API key from the environment variable
# Get the path to the API key
current_directory = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.abspath(os.path.join(current_directory, '..\SencibleDATA', 'accountactivity.csv'))

# Load the CSV file
df = pd.read_csv(data_file_path)

# Ensure the second column is used for grouping
if len(df.columns) < 2:
    raise ValueError("The CSV file does not have at least two columns.")

description_column = df.columns[1]  # Second column

# Group by the 'DESCRIPTION' column and count occurrences
grouped_df = df.groupby(description_column).size().reset_index(name='Count')

datename= datetime.now().strftime('%Y%m%d_%H%M%S')
file_name = f'output_{datename}.csv'

file_path = os.path.join(os.path.join(current_directory, '..\SencibleDATA'), file_name)  # Full path

# Save the DataFrame to a CSV file
grouped_df.to_csv(file_path, index=False)



