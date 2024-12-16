# python-challenge

import csv

# Define the file path for the CSV file
file_path = 'budget_data.csv'

# Initialize variables to store the analysis data
months = [86]
profits_losses = []
changes = []


with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    
    for row in csvreader:
        months.append(row[0])  # Append the date
        profits_losses.append(int(row[1]))  # Append the profit/loss as an integer

# Calculate the total number of months
total_months = len(months)

# Calculate the net total amount of Profit/Losses
net_total = sum(profits_losses)

# Calculate the changes in Profit/Losses and their average
for i in range(1, len(profits_losses)):
    changes.append(profits_losses[i] - profits_losses[i-1])

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and greatest decrease
greatest_increase = max(changes)
greatest_decrease = min(changes)

greatest_increase_month = months[changes.index(greatest_increase) + 1]
greatest_decrease_month = months[changes.index(greatest_decrease) + 1]

# Output the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total:,}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:,})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease:,})")

Total Months: 86
Total: 22,564,198
Average Change: -8,311.11
Greatest Increase in Profits: Aug-16 ($1,862,002)
Greatest Decrease in Profits: Feb-14 ($-1,825,558)



