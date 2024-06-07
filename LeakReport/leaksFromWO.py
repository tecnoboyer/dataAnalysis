import pandas as pd

woOrders_history = pd.read_excel('n:\\CI\\5S Program\\5S Master Folder\\Leonardo\\Leaks\\woHistory_from2020.xlsx')
dept_counts = woOrders_history['Dept.'].value_counts()



equipment_counts = woOrders_history.groupby(['Dept.','Equipment','Status']).nunique()
Details = woOrders_history.groupby(['Dept.','Equipment','Description','Status']).nunique()
print(equipment_counts)

# equipment_counts.to_csv('n:\\CI\\5S Program\\5S Master Folder\\Leonardo\\Analysis\\Leaks\\groupedbyMachine_status.csv')

Details.to_csv('n:\\CI\\5S Program\\5S Master Folder\\Leonardo\\Analysis\\Leaks\\Details2.csv')

# print(equipment_counts)