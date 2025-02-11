import pandas as pd
import os 

current_directory = os.path.dirname(os.path.abspath(__file__))
statement_path = os.path.abspath(os.path.join(current_directory, '..\SencibleDATA', 'EmmaStatements.csv'))
statement = pd.read_csv(statement_path)
expected_columns = ["Date", "Description", "Debt", "Credit", "Balance"]
statement.columns = expected_columns

# Assuming that csvList has the REMAINING not trained


# Convert 'Date' column to datetime for easier grouping
statement["Date"] = pd.to_datetime(statement["Date"])

# Filter rows with a value in the 'Credit' column
credit_rows = statement[statement["Credit"].notna()]

# Group by month and calculate the total of the 'Credit' column
# credit_by_month = credit_rows.groupby(credit_rows["Date"].dt.to_period("M"))["Credit"].sum()
credit_by_description = credit_rows.groupby(credit_rows["Description"])["Credit"].sum()

# Print the result
print("Total Credit by Month:")
print(credit_by_description)

# print(statement.head(3))
