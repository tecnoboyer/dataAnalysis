import pandas as pd


file_path = 'N:\\CI\\5S Program\\Training\\Analysis\\doneList.csv'


done = pd.read_csv(file_path)


file_path2 = 'N:\\CI\\5S Program\\Training\\Analysis\\Reference.xlsx'
etq = pd.read_excel(file_path2)



# filtered_df2 = done[done['First Name'].~isin(etq['First Name'])]

filtered_df2 = done[done['First Name'].isin(etq['First Name'])]
filtered_df3 = done[~done['First Name'].isin(etq['First Name'])]


# print(filtered_df2.head())

filtered_df2.to_csv('N:\\CI\\5S Program\\Training\\Analysis\\include.csv')
filtered_df2.to_csv('N:\\CI\\5S Program\\Training\\Analysis\\exclude.csv')



