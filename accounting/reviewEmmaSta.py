import pandas as pd
statement = pd.read_csv('C:\\Users\\technoboyer\\Documents\\CasaCuentas\\EmmaStatements\\EmmaStatements.csv')
expected_columns = ["Date", "Description", "Debt", "Credit", "Balance"]
statement.columns = expected_columns

# Assuming that csvList has the REMAINING not trained

# Next list represents the include roles or position 
# job_titles_to_filter = [
#     'Manufacturing Technician', 'Production Associate', 'PMC PRODUCTION ASSOCIATE',
#     'Operations Technician - Millwright', 'PMC SETUP PA', 'Gauge Technician',
#     'MATERIAL HANDLER', 'Manufacturing Support Setup PA', 'Tool Room Support',
#     'PMC SET UP PA',  'PMC TEAM LEADER', 'CMM OPERATOR', 'Powder Tech', 'Rig Setup PA', 'Dorst Maintenance Technician',
#     'Maintenance Planner', 'Operation Technician',
#     'Electrical Co-op', 'Manufacturing Technician (Finishing)', 
#     'Press Rig Set Up PA', 'Operations Technician', 'Cinci Maintenance Technician',
#     'OPERATIONS SUPPORT SPECIALIST', 'Process Monitor',
#     'Customer Service/Materials Coordinator', 'Manufacturing Technician Student',
#     'Tool Crib Attendant', 'MILLWRIGHT APPRENTICE', 'Document and Data Control Specialist',
#     'Quality Technician', 'Tool Design Specialist', 'Electrical PLC/Control Specialist', 'Tool and Die Technician', 'Tool and Die Apprentice',  
#     'Lubrication Technician', 'Powder Technician', 'Operations Technician Electrician'
# ]

# statement.to_csv('C:\\Users\\technoboyer\\Documents\\CasaCuentas\\EmmaStatements\\proccessed.csv', index=False)

# Convert 'Date' column to datetime for easier grouping
statement["Date"] = pd.to_datetime(statement["Date"])

# Filter rows with a value in the 'Credit' column
credit_rows = statement[statement["Credit"].notna()]

# Group by month and calculate the total of the 'Credit' column
credit_by_month = credit_rows.groupby(credit_rows["Date"].dt.to_period("M"))["Credit"].sum()

# Print the result
print("Total Credit by Month:")
print(credit_by_month)

# print(statement.head(3))
