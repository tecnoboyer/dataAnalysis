import pandas as pd

df = pd.read_csv('may.csv')

df['Date Reported'] = pd.to_datetime(df['Date Reported'])

start_date = pd.to_datetime('2024-04-01')
filtered_df = df[df['Date Reported'] > start_date]


filtered_df2 = filtered_df[filtered_df['Description'].str.contains('coolant|air|water', case=False)]



print(f'Number of workorder created: {filtered_df2.describe()}')
filtered_df2.to_csv('C:\\Users\\leonardo.boyersojo\\Documents\\5S\\Program\\LeakReport\\potential.csv')
