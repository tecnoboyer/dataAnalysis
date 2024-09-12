import pandas as pd

everybody = pd.read_csv('n:\\CI\\5S Program\\Training\\Analysis\\csvList2.csv')
# Assuming that csvList has the REMAINING not trained

# Next list represents the include roles or position 
job_titles_to_filter = [
    'Manufacturing Technician', 'Production Associate', 'PMC PRODUCTION ASSOCIATE',
    'Operations Technician - Millwright', 'PMC SETUP PA', 'Gauge Technician',
    'MATERIAL HANDLER', 'Manufacturing Support Setup PA', 'Tool Room Support',
    'PMC SET UP PA',  'PMC TEAM LEADER', 'CMM OPERATOR', 'Powder Tech', 'Rig Setup PA', 'Dorst Maintenance Technician',
    'Maintenance Planner', 'Operation Technician',
    'Electrical Co-op', 'Manufacturing Technician (Finishing)', 
    'Press Rig Set Up PA', 'Operations Technician', 'Cinci Maintenance Technician',
    'OPERATIONS SUPPORT SPECIALIST', 'Process Monitor',
    'Customer Service/Materials Coordinator', 'Manufacturing Technician Student',
    'Tool Crib Attendant', 'MILLWRIGHT APPRENTICE', 'Document and Data Control Specialist',
    'Quality Technician', 'Tool Design Specialist', 'Electrical PLC/Control Specialist', 'Tool and Die Technician', 'Tool and Die Apprentice',  
    'Lubrication Technician', 'Powder Technician', 'Operations Technician Electrician'
]



filtered_jobs = everybody[everybody['Job'].isin(job_titles_to_filter)]

etqList = pd.read_csv('n:\\CI\\5S Program\\Training\\Analysis\\etqRegist.csv')
etqList['FistName']=etqList['Employee Name'].str.split(' ', expand=True)[0]
etqList['surName']=etqList['Employee Name'].str.split(' ', expand=True)[1]
etqList.rename(columns={'FistName': 'First Name', 'surName': 'Last Name'}, inplace=True)


merged_df = everybody.merge(etqList[['First Name', 'Last Name']], on=['First Name', 'Last Name'], how='left', indicator=True)

result_df = merged_df[merged_df['_merge'] == 'left_only'].drop(columns=['_merge'])
print(result_df)


# # I need to resolve those where the surname is the [2}] split


# dayShift = filtered_jobs[filtered_jobs['Shift Rotation Name'].str.contains('Day')]
# aftShift = filtered_jobs[filtered_jobs['Shift Rotation Name'].str.contains('Aft')]
# ngtShift = filtered_jobs[filtered_jobs['Shift Rotation Name'].str.contains('Ngt')]
# not_shift = filtered_jobs[~filtered_jobs['Shift Rotation Name'].str.contains('Day|Aft|Ngt')]


result_df.to_csv('n:\\CI\\5S Program\\Training\\result_df.csv', index=False)
# aftShift.to_csv('n:\\CI\\5S Program\\Training\\aftShift.csv', index=False)
# ngtShift.to_csv('n:\\CI\\5S Program\\Training\\ngtShift.csv', index=False)
# not_shift.to_csv('n:\\CI\\5S Program\\Training\\not_shift.csv', index=False)


# print(filtered_jobs['Employee #'].count())

