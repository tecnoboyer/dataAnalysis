import pandas as pd

file_path = 'N:\\CI\\5S Program\\Red Tag Process\\Virtual Red Tag.xlsx'

# Read the Excel file
df_raw = pd.read_excel(file_path, header=None)

# Extract relevant rows and columns
data = {
    'Red Tagged By?': [df_raw.iloc[0, 2]],
    'Red Tagged from What Area/Machine:': [df_raw.iloc[0, 6]],
    'Date Item Tagged?': [df_raw.iloc[2, 2]],
    'Where is the Item Located Now?': [df_raw.iloc[2, 6]],
    'Item Name': [df_raw.iloc[4, 1]],
    'Item Advisor': [df_raw.iloc[4, 5]],
    'Item Description': [df_raw.iloc[6, 1]],
    'Primary Asset #': [df_raw.iloc[6, 5]],
    'Disposition': [df_raw.iloc[8, 1]],
    'Assign To': [df_raw.iloc[10, 1]],
    'Done': [df_raw.iloc[10, 3]],
    'Comment': [df_raw.iloc[12, 1]],
    'Tooling Owner?': [df_raw.iloc[12, 5]]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)