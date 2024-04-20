import pandas as pd
pd.set_option('future.no_silent_downcasting', True)
# Load the CSV file
file_path = 'C:/Users/Claflin/Desktop/dfg/Consolidated_Educational_Data.csv'
data = pd.read_csv(file_path)

# Group the data by 'Zip Code' and sum the 'StudentEnrollment' for each group
enrollment_by_zip = data.groupby('Zip Code')['StudentEnrollment'].sum().reset_index()

# Save the new DataFrame to a CSV file
enrollment_by_zip.to_csv('Summed_Enrollment_by_Zip.csv', index=False)

