import pandas as pd
import matplotlib.pyplot as plt

# Define the file path for the new file to create
new_file_path = 'C:/Users/Claflin/Desktop/dfg/Philadelphia_Data.csv'

# Load the filtered and sorted dataset
philadelphia_data = pd.read_csv(new_file_path)

# Ensure the data is sorted (if it is not already from the previous steps)
philadelphia_data = philadelphia_data.sort_values(by='est', ascending=True)

# Plotting
plt.figure(figsize=(12, 8))  # Set the figure size for better readability
ax = plt.subplot(111)  # Create a subplot and store its axes object in 'ax'
ax.bar(philadelphia_data['zip'], philadelphia_data['est'], color='orange')  # Use a contrasting bar color
ax.set_facecolor('black')  # Set the background color of the axes
plt.gcf().set_facecolor('black')  # Set the background color of the figure

# Setting labels and title with a light color for visibility
plt.xlabel('ZIP Code', color='white')  # X-axis label
plt.ylabel('Total Number of Establishments', color='white')  # Y-axis label
plt.title('Number of Establishments by ZIP Code in Philadelphia', color='white')  # Title of the graph

# Customize the tick marks
ax.tick_params(colors='white', which='both')  # Change the color of the ticks to white

# Rotate the ZIP codes for better visibility
plt.xticks(rotation=45)

# Adjust the layout to make room for the rotated x-axis labels
plt.tight_layout()

# Display the plot
plt.show()