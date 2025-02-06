import pandas as pd

# Load the CSV file
df = pd.read_csv('account.csv')

# Ensure the second column is used for grouping
if len(df.columns) < 2:
    raise ValueError("The CSV file does not have at least two columns.")

description_column = df.columns[1]  # Second column

# Group by the 'DESCRIPTION' column and count occurrences
grouped_df = df.groupby(description_column).size().reset_index(name='Count')

# Display the grouped data
print(grouped_df)