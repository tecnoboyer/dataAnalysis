import pandas as pd

everybody = pd.read_csv('n:\\CI\\5S Program\\Training\\Analysis\\csvList2.csv')
# Assuming that csvList2 has the UPDATED HHRR employees

# Next list represents the include roles or position 
job_titles_to_filter = [
    'Manufacturing Technician', 'Production Associate', 'PMC PRODUCTION ASSOCIATE',
    'Operations Technician - Millwright', 'PMC SETUP PA', 'Gauge Technician',
    'MATERIAL HANDLER', 'Manufacturing Support Setup PA', 'Tool Room Support',
    'PMC SET UP PA',  'PMC TEAM LEADER', 'CMM OPERATOR', 'Powder Tech', 'Rig Setup PA', 'Dorst Maintenance Technician',
    'Maintenance Planner', 'Operation Technician',
    'Electrical Co-op', 'Manufacturing Technician (Finishing)', 
    'Press Rig Set Up PA', 'Operations Technician', 'Cinci Maintenance Technician', 'Process Monitor', 'Manufacturing Technician Student',
    'Tool Crib Attendant', 'MILLWRIGHT APPRENTICE',
    'Quality Technician', 'Tool Design Specialist', 'Electrical PLC/Control Specialist', 'Tool and Die Technician', 'Tool and Die Apprentice',  
    'Lubrication Technician', 'Powder Technician', 'Operations Technician Electrician'
]



filtered_jobs = everybody[everybody['Job'].isin(job_titles_to_filter)]
# filtered_jobs.to_csv('n:\\CI\\5S Program\\Training\\filtered_jobs.csv', index=False)
etqList = pd.read_csv('n:\\CI\\5S Program\\Training\\Analysis\\allETQ.csv')
#    #####///Coment
# etqRegist2.csv stand for the ETQ last update
# Go ETQ, Download the Part5 : ... & Completed,Get rid of the first 5 line ( just left the header with the column names as is). 

etqList['FistName']=etqList['Employee Name'].str.split(' ', expand=True)[0]
etqList['surName']=etqList['Employee Name'].str.split(' ', expand=True)[1]
etqList.rename(columns={'FistName': 'First Name', 'surName': 'Last Name'}, inplace=True)
# etqList.to_csv('n:\\CI\\5S Program\\Training\\etqListBefore2.csv', index=False)


merged_df = filtered_jobs.merge(etqList[['First Name', 'Last Name']], on=['First Name', 'Last Name'], how='left', indicator=True)

# Perform the merge
merged_df = filtered_jobs.merge(etqList[['First Name', 'Last Name']], on=['First Name', 'Last Name'], how='left', indicator=True)

# Filter the rows that are in filtered_jobs but not in etqList
result_df = merged_df[merged_df['_merge'] == 'left_only']

# Drop the '_merge' column if you don't need it
result_df = result_df.drop(columns=['_merge'])

result_df.to_csv('n:\\CI\\5S Program\\Training\\noregisteredETQ.csv', index=False)






