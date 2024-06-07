
import pandas as pd

df = pd.read_csv('workOrders.csv')

df['Date Reported'] = pd.to_datetime(df['Date Reported'])

start_date = pd.to_datetime('2024-03-29')
end_date = pd.to_datetime('2024-05-01')
filtered_df = df[df['Date Reported'] > start_date]
filtered_df2 = filtered_df[filtered_df['Date Reported'] < end_date]

# filtered_df2 = filtered_df[filtered_df['Description'] == 'leak']

total = filtered_df2[filtered_df2['Description'].str.contains('leak', case=False)]

completed = total[total['Status'].str.contains('Comp', case=False)]


print(f'Number of workorder created: {total.describe()}')
print(f'Number of solved workorder : {completed.describe()}')
