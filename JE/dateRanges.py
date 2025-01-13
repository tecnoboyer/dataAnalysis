
import pandas as pd

# Replace 'FILE_PATH_OR_URL' with the actual path or URL of your Excel file
df = pd.read_csv('workOrders.csv')

df['Date Reported'] = pd.to_datetime(df['Date Reported'])

start_date = pd.to_datetime('2024-04-01')
filtered_df = df[df['Date Reported'] > start_date]

print(filtered_df.describe())

