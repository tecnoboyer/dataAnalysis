import pandas as pd

woOrders_history = pd.read_excel('n:\\CI\\5S Program\\5S Master Folder\\Leonardo\\Leaks\\woHistory_from2020.xlsx')
# dept_counts = woOrders_history['Dept.'].value_counts()



# equipment_counts = woOrders_history.groupby(['Dept.','Equipment','Status']).nunique()
# Details = woOrders_history.groupby(['Dept.','Equipment','Description','Status']).nunique()
# print(equipment_counts)
# Date Reported


# equipment_counts = woOrders_history.groupby(['Dept.','Equipment','Status']).nunique()

# equipment_counts.to_csv('n:\\CI\\5S Program\\5S Master Folder\\Leonardo\\Analysis\\Leaks\\groupedbyMachine_status.csv')

# Details.to_csv('n:\\CI\\5S Program\\5S Master Folder\\Leonardo\\Analysis\\Leaks\\Details2.csv')

# print(equipment_counts)

# Assuming 'df' is your DataFrame and it's already loaded with data
# Convert 'Date Reported' to datetime
woOrders_history['Date Reported'] = pd.to_datetime(woOrders_history['Date Reported'])

woOrders_completed=woOrders_history
woOrders_completed['Date Reported'] = pd.to_datetime(woOrders_completed['Date Completed'])

# Extract year and month from 'Date Reported'
woOrders_history['YearMonth'] = woOrders_history['Date Reported'].dt.to_period('M')
woOrders_completed['YearMonth'] = woOrders_completed['Date Completed'].dt.to_period('M')


# Filter the DataFrame for rows where 'Status' is 'completed'
completed_orders = woOrders_completed[woOrders_completed['Status'] == 'completed']

# Group by 'YearMonth' and count the occurrences of 'completed' status per 'YearMonth'
completed_status_counts_per_month = completed_orders.groupby('YearMonth').size().reset_index(name='Count')



status_counts_per_month = woOrders_history.groupby(['YearMonth', 'Status']).size().reset_index(name='Count')


status_counts_per_month.to_csv('n:\\CI\\5S Program\\5S Master Folder\\Leonardo\\Leaks\\StatusPerMonth2.csv')
completed_status_counts_per_month.to_csv('n:\\CI\\5S Program\\5S Master Folder\\Leonardo\\Leaks\\justCompleted.csv')

