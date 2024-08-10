import pandas as pd


file_path = 'N:\\CI\\5S Program\\Red Tag Process\\Virtual Red Tag.xlsx'

df = pd.read_excel(file_path, header=None)


# Initialize an empty list to store the DataFrames for each section
dfs = []

# Initialize a flag to track whether we are inside a section
inside_section = False

# Iterate over the DataFrame rows
for i, row in df.iterrows():
    print(i , row)

    # # Check if the row contains 'Red Tagged By?'
    # if 'Red Tagged By?' in str(row[0]) in row:
    #     # Start of a new section
    #     inside_section = True
    #     section_df = pd.DataFrame(columns=[0, 1])  # Initialize an empty DataFrame
    # elif inside_section:
    #     # Add rows to the section DataFrame until an empty row is encountered
    #     if row[0] is not None:
    #         section_df = section_df.append(row[:2], ignore_index=True)
    #     else:
    #         # End of the section
    #         inside_section = False
    #         dfs.append(section_df)






print(dfs)
