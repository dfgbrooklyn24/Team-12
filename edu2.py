import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'C:/Users/Claflin/Desktop/dfg/Consolidated_Educational_Data.csv'
data = pd.read_csv(file_path)

# Group the data by 'Zip Code' and sum the 'StudentEnrollment' for each group
enrollment_by_zip = data.groupby('Zip Code')['StudentEnrollment'].sum().reset_index()

# Set up the figure and axis for the plot
plt.figure(figsize=(10, 6))

# Create a bar graph of the summed enrollments by ZIP code
plt.bar(enrollment_by_zip['Zip Code'].astype(str), enrollment_by_zip['StudentEnrollment'], color='skyblue')

# Add labels and title
plt.xlabel('Zip Code')
plt.ylabel('Student Enrollment')
plt.title('Summed Student Enrollment by Zip Code')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better visibility

# Show the plot
plt.tight_layout()
plt.show()

# Optionally, save the graph as an image
plt.savefig('Enrollment_by_Zip_Code.png')
