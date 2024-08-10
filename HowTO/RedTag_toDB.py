import pandas as pd
from datetime import datetime

# Define the path to the xlsx file
file_path = 'N:\\CI\\5S Program\\Red Tag Process\\copilotTest.xlsx'


acumulator_path= 'N:\\CI\\5S Program\\Red Tag Process\\RedTag_LOG_Acumulator.csv'
acumulator = pd.read_csv(acumulator_path)
# print(acumulator.columns)


# Read the xlsx file
df = pd.read_excel(file_path, header=None)
# print(df)

# Extract the values for each column based on the provided structure
red_tagged_by = df.iloc[0, 1]
red_tagged_from = df.iloc[0, 5]
red_tagged_date = df.iloc[2, 1]
item_location = df.iloc[2, 4]
item_name = df.iloc[4, 1]
item_advisor = df.iloc[4, 5]
item_description = df.iloc[6, 1]
primary_asset = df.iloc[6, 5]
disposition = df.iloc[8, 1]
component_asset = df.iloc[8, 5]
asingTo = df.iloc[10, 2]
done= df.iloc[10, 2]
tooling_Serial=df.iloc[10,5] 
comment=df.iloc[12,1]
tooling_owner=df.iloc[12,5]





# Create a new dataframe with the specified columns
data = {
    'Item#': ['tbd'],
    'RT#': ['tbd'],
    'Primary  Asset #':[primary_asset],
    'Component ASSET #':[component_asset],
    'Area/Machine': [red_tagged_from],
    'Located Now (Current location)': [item_location],
    'Item Name': [item_name],
    'Item Description': [item_description],
    'Logical Located ': ['tbd'],
    'Last review': ['tbd'],
    'Asset Status':[disposition],
    'Disposition date (as applicable)': ['tbd'],
    'tooling_owner':[tooling_owner]
}
# Convert the dictionary to a DataFrame
result_df = pd.DataFrame(data)
# print(result_df.columns)
# print(acumulator.columns)
# print('/////')
# print(result_df.head(2))

concatenated_df = pd.concat([acumulator, result_df], ignore_index=True)
# print(concatenated_df.head(56))

# # csv_file_name = f"acumulator_{date_stamp}.csv"
concatenated_df.to_csv('N:\\CI\\5S Program\\Red Tag Process\\RedTag_LOG_Acumulator.csv', index=False)