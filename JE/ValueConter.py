# COUNTING THE CATEGORIES

import pandas as pd

# Replace 'FILE_PATH_OR_URL' with the actual path or URL of your Excel file
df = pd.read_csv('workOrders.csv')


category_counts = df['Status'].value_counts()

print(category_counts)


