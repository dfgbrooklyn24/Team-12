import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'C:/Users/Claflin/Desktop/dfg/Book1.csv'
try:
    # Load data from the CSV file, ensuring that column names are trimmed of any extra whitespace
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()  # Strip any extra spaces from column names
except Exception as e:
    print(f"Error loading CSV file: {e}")
    data = pd.DataFrame()  # Create an empty DataFrame if there's an issue

# Check if the DataFrame is not empty
if not data.empty:
    # Sort the data by 'Number of Population' in descending order to order the bars
    data_sorted = data.sort_values(by='Median Income', ascending=True)

    # Plotting the data
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Creating a bar graph for Number of Population
    color = 'tab:blue'
    ax1.set_xlabel('Zip Code')
    ax1.set_ylabel('Median Income', color=color)
    ax1.bar(data_sorted['Zip Code'].astype(str), data_sorted['Median Income'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    # Creating a second y-axis for Number of Schools using the same x-axis
    ax2 = ax1.twinx()  
    color = 'tab:red'
    ax2.set_ylabel('Number of enrollment', color=color)  
    ax2.plot(data_sorted['Zip Code'].astype(str), data_sorted['Number of enrollment'], color=color, marker='o')
    ax2.tick_params(axis='y', labelcolor=color)

    # Title of the graph
    plt.title('Median Income and number of enrollment by zip code in Philadelphia (under 10 miles radius from current ZIP)')

    # Show the plot
    plt.tight_layout()
    plt.show()

else:
    print("No data loaded. Check file path and ensure CSV file is correctly formatted.")


