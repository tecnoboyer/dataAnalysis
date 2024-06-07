

# import pandas as pd

# # Specify the path to your Excel file
# excel_file_path = 'N:\\CI\\5S Program\\Champions\\Cell 1 Manjinder M\\Cell 1 Fluid, Powder & Air Leak Log.xlsx'

# # Read the Excel file into a DataFrame, skipping the first two rows
# df = pd.read_excel(excel_file_path, skiprows=[0, 1])

# # Exclude columns greater than column L (columns 13 and beyond)
# df = df.iloc[:, :13]  # Keep columns up to column L (index 12)

# # Display the modified DataFrame
# print(df)

# **********
# import os

# # Specify the root directory where you want to search
# root_directory = r'N:\CI\5S Program\Champions'

# # Initialize an empty list to store file paths
# file_paths = []

# # Recursively search for files with the specified name
# for foldername, subfolders, filenames in os.walk(root_directory):
#     for filename in filenames:
#         if 'Fluid, Powder & Air Leak Log' in filename:
#             file_paths.append(os.path.join(foldername, filename))

# # Print the list of matching file paths
# for path in file_paths:
#     print(path)
# *******

# import pandas as pd
# import os as os

# # Initialize an empty list to store DataFrames
# all_dfs = []
# root_directory = r'N:\CI\5S Program\Champions'

# for foldername, subfolders, filenames in os.walk(root_directory):
#     for filename in filenames:
#         if 'Fluid, Powder & Air Leak Log' in filename:
#             print(f'list of files ${filename}')
#             file_path = os.path.join(foldername, filename)
#             df = pd.read_excel(file_path, skiprows=[0, 1])
#             all_dfs.append(df)
#             concatenated_df = pd.concat(all_dfs, axis=1)

# # Display the concatenated DataFrame
# print(concatenated_df.describe())



# ********



# import pandas as pd
# from pathlib import Path

# # Specify the root directory where you want to search
# root_directory = r'N:\CI\5S Program\Champions'

# # Initialize an empty list to store DataFrames
# all_dfs = []

# # Use pathlib to traverse subfolders and find Excel files
# p = Path(root_directory)
# for f in p.glob('**/*Fluid, Powder & Air Leak Log*.xlsx'):
#     # print(f'list of files ${f}')
#     df = pd.read_excel(f, skiprows=[0, 1])
#     all_dfs.append(df)
# concatenated_df = pd.concat(all_dfs, axis=1)

# # Display the concatenated DataFrame
# # print(all_dfs)
# print(concatenated_df)


# **********************

import pandas as pd
from pathlib import Path

# Specify the root directory where you want to search
root_directory = r'N:\CI\5S Program\Champions'

# Initialize an empty list to store DataFrames
all_dfs = []

# Use pathlib to traverse subfolders and find Excel files
p = Path(root_directory)
for f in p.glob('**/*Fluid, Powder & Air Leak Log*.xlsx'):
    df = pd.read_excel(f, skiprows=[0, 1])
    all_dfs.append(df)

# Concatenate DataFrames horizontally
concatenated_df = pd.concat(all_dfs, axis=1)

# Reset index for concatenated DataFrame
concatenated_df.reset_index(drop=True, inplace=True)

# Display the concatenated DataFrame
print(concatenated_df)

