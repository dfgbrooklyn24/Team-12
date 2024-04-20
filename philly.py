import pandas as pd

# Set pandas option to not suppress downcasting warnings
pd.set_option('future.no_silent_downcasting', True)

# Define the file path for the original data and the new file to create
original_file_path = 'C:/Users/Claflin/Desktop/dfg/Nonprofit_Data_PA.csv'
new_file_path = 'C:/Users/Claflin/Desktop/dfg/Philadelphia_Data.csv'


# Load the dataset
data = pd.read_csv(original_file_path)
print("Data loaded successfully.")

# Filter for rows where the 'CITY' column matches 'Philadelphia'
# Adjust the column name if needed to match the exact name in your CSV file
philadelphia_data = data[data['city'].str.lower() == 'philadelphia']

# Ensure 'est' is numeric (in case there are non-numeric values present)
# Adjust the 'est' column name if needed to match the exact name in your CSV file
philadelphia_data['est'] = pd.to_numeric(philadelphia_data['est'], errors='coerce').fillna(0)

# Sort the filtered DataFrame by the 'est' column in ascending order
# This keeps all columns intact, including ZIP code and others
philadelphia_data_sorted = philadelphia_data.sort_values(by='est', ascending=True)

# Save the sorted DataFrame to a new CSV file
philadelphia_data_sorted.to_csv(new_file_path, index=False)

print("Philadelphia data sorted by total number of establishments in ascending order and saved to a new file.")
