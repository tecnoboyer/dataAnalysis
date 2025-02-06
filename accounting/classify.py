import pandas as pd
import os
from datetime import datetime

# Set your OpenAI API key from the environment variable
# Get the path to the API key
current_directory = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.abspath(os.path.join(current_directory, '..\SencibleDATA', 'accountactivity.csv'))

# current_directory = os.path.dirname(os.path.abspath(__file__))
# api_key_file_path = os.path.abspath(os.path.join(current_directory, '..', 'API_KEY.txt'))



# Load the CSV file
df = pd.read_csv(data_file_path)

# Ensure the second column is used for grouping
if len(df.columns) < 2:
    raise ValueError("The CSV file does not have at least two columns.")

description_column = df.columns[1]  # Second column

# Group by the 'DESCRIPTION' column and count occurrences
grouped_df = df.groupby(description_column).size().reset_index(name='Count')

datename= datetime.now().strftime('%Y%m%d_%H%M%S')

file_path = os.path.join(data_file_path, datename)  # Full path

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)



