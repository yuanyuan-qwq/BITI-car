import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('CARCAR.xlsx')

# Get user input for the date range in DD/MM/YYYY format
start_date = input("Enter the start date (DD/MM/YYYY): ")
end_date = input("Enter the end date (DD/MM/YYYY): ")

# Convert user input dates to datetime objects with the DD/MM/YYYY format
start_date = pd.to_datetime(start_date, format='%d/%m/%Y')
end_date = pd.to_datetime(end_date, format='%d/%m/%Y')

# Filter the DataFrame based on the date range
filtered_df = df[(df['DATE'] >= start_date) & (df['DATE'] <= end_date)]

# Create a dictionary to store passenger counts
passenger_counts = {}

# Initialize the total passenger count
total_passenger_count = 0

# Iterate through the filtered DataFrame to count passengers
for passengers in filtered_df['passenger ']:
    passenger_list = passengers.split(', ')
    total_passenger_count += len(passenger_list)
    for passenger in passenger_list:
        if passenger in passenger_counts:
            passenger_counts[passenger] += 1
        else:
            passenger_counts[passenger] = 1

# Display the filtered data
print("Filtered Data:")
print(filtered_df)
print("\n")
# Display the passenger counts
print("Passenger Counts:")
for passenger, count in passenger_counts.items():
    print(f"{passenger}: {count} times")

# Display the total passenger count
print(f"\nTotal passenger count in the selected date range: {total_passenger_count}")

# Get user input for the total price
total_price = float(input("Enter the total price: "))

# Calculate and display the payment for each passenger
print("\nPayment for Each Passenger:")
for passenger, count in passenger_counts.items():
    payment = total_price * (count / total_passenger_count)
    print(f"{passenger}: {payment:.2f}")

