
import pandas as pd

df = pd.read_csv('workOrders.csv')

df['Date Reported'] = pd.to_datetime(df['Date Reported'])

start_date = pd.to_datetime('2024-04-01')
filtered_df = df[df['Date Reported'] > start_date]

# filtered_df2 = filtered_df[filtered_df['Description'] == 'leak']

filtered_df2 = filtered_df[filtered_df['Description'].str.contains('leak', case=False)]

filtered_df3 = filtered_df2[filtered_df2['Status'].str.contains('Comp', case=False)]


print(f'Number of workorder created: {filtered_df2.describe()}')
print(f'Number of solved workorder : {filtered_df3.describe()}')
