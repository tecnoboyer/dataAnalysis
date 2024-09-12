import pandas as pd

everybody = pd.read_csv('n:\\CI\\5S Program\\Training\\Analysis\\csvList.csv')
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

dayLeet = ['Day']

filtered_jobs = everybody[everybody['Job'].isin(job_titles_to_filter)]

dayShift = filtered_jobs[filtered_jobs['Shift Rotation Name'].str.contains('Day')]
aftShift = filtered_jobs[filtered_jobs['Shift Rotation Name'].str.contains('Aft')]
ngtShift = filtered_jobs[filtered_jobs['Shift Rotation Name'].str.contains('Ngt')]
not_shift = filtered_jobs[~filtered_jobs['Shift Rotation Name'].str.contains('Day|Aft|Ngt')]


dayShift.to_csv('n:\\CI\\5S Program\\Training\\dayShift.csv', index=False)
aftShift.to_csv('n:\\CI\\5S Program\\Training\\aftShift.csv', index=False)
ngtShift.to_csv('n:\\CI\\5S Program\\Training\\ngtShift.csv', index=False)
not_shift.to_csv('n:\\CI\\5S Program\\Training\\not_shift.csv', index=False)


# print(filtered_jobs['Employee #'].count())

