import pandas as pd


file_path = 'N:\\CI\\5S Program\\Training\\Analysis\\noDone.csv'
not_done = pd.read_csv(file_path)

not_done['name'] = not_done['First Name'] + ' ' + not_done['Last Name']


file_path2 = 'N:\\CI\\5S Program\\Training\\Analysis\\etqDone.csv'
etq = pd.read_csv(file_path2)



print ( not_done.head())

drop_those = not_done[not_done['name'].isin(etq['Employee Name'])]

rescue = not_done[~not_done['name'].isin(etq['Employee Name'])]

# filtered_df2 = done[done['First Name'].isin(etq['First Name'])]
# filtered_df3 = done[~done['First Name'].isin(etq['First Name'])]


# # print(filtered_df2.head())

# drop_those.to_csv('N:\\CI\\5S Program\\Training\\Analysis\\drop_those.csv')
rescue.to_csv('N:\\CI\\5S Program\\Training\\Analysis\\rescue.csv')



