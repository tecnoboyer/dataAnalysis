
import pandas as pd


file_path = 'C:\\Users\\leonardo.boyersojo\\Documents\\5S\\Program\\dataAnalysisManufactoring\\ToolinMatter\\paraleer.xlsx'

# N:\\Operations\\Material Planning\\Inventory\\Daily Inventory\\Daily Inventory History\\2008 Daily inventories\\April 2008\\April 8, 2008.xls'

filePath2='N:\\Operations\\Material Planning\\Inventory\\Daily Inventory\\Daily Inventory History\\2012 Daily inventories\\February\\Feb 1.xls'



# excel_file = pd.ExcelFile(filePath2)

# # Get the list of sheet names
# sheet_names = excel_file.sheet_names

# first_sheet_df = excel_file.parse(sheet_names[0])

# print("\nFirst few rows of the first sheet:")
# print(first_sheet_df.columns)

# # Print the sheet names
# print(f"Sheet names in the Excel file: {sheet_names}")
# # dept_counts = woOrders_history['Dept.'].value_counts()


# df['Date Reported'] = pd.to_datetime(df['Date Reported'])

# start_date = pd.to_datetime('2024-03-29')
# end_date = pd.to_datetime('2024-05-01')
# filtered_df = df[df['Date Reported'] > start_date]
# filtered_df2 = filtered_df[filtered_df['Date Reported'] < end_date]

# # filtered_df2 = filtered_df[filtered_df['Description'] == 'leak']

# total = filtered_df2[filtered_df2['Description'].str.contains('leak', case=False)]

# completed = total[total['Status'].str.contains('Comp', case=False)]


# print(f'Number of workorder created: {total.describe()}')
# print(f'Number of solved workorder : {completed.describe()}')




# Load the entire sheet into a DataFrame without using the first row as headers
df = pd.read_excel(filePath2, header=None)

# Initialize an empty list to store the DataFrames for each section
dfs = []

# Initialize a flag to track whether we are inside a section
inside_section = False

# Iterate over the DataFrame rows
for i, row in df.iterrows():
    # Check if the row contains 'Part Number' and 'Description'
    if 'Part Number' in str(row[0]) and 'Description' in str(row[1]):
        # Start of a new section
        inside_section = True
        section_df = pd.DataFrame(columns=[0, 1])  # Initialize an empty DataFrame
    elif inside_section:
        # Add rows to the section DataFrame until an empty row is encountered
        if row[0] is not None:
            section_df = section_df.append(row[:2], ignore_index=True)
        else:
            # End of the section
            inside_section = False
            dfs.append(section_df)

# Concatenate all section DataFrames into one
final_df = pd.concat(dfs, ignore_index=True)

# Display the final DataFrame
print(final_df)

