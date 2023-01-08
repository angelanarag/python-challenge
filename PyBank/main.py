# Analyze and calculates the following using the budget_data.csv file
#  - Total number of months included in the dataset
#       Step 1: Create a variable for total_months
#       Step 2: Count how many months are in the Date Column
#  - Net total amount of Profit/Loss over the entire period
#       Step 1: Create a variable for total_pl
#       Step 2: Sum the values in the Profit/Losses Column
#  - Changes in P&L over the entire period, then average the changes
#       Step 1: Create variables
#  - Greatest increase in profits (date and amount) over the entire period
#  - Greatest decrease in profits (date and amount) over the entire period

# Import the modules
import os
import csv

# Set file path to budget_data.csv 
budget_file = os.path.join("Resources", "budget_data.csv")

# Set output of the file
budget_output = os.path.join("analysis", "budget_output.txt")

# Set variables

months = []
pl = []
pl_change = []
pl_average = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
month_of_change = []



# Open the csv file
with open(budget_file) as csvfile:

    # Specify delimiter and variable that holds contents of the csv file
    budgetreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first and skip to next so you don't include it in the count
    skip_header = next(budgetreader)

    # Go through the rows in the budget data file
    for row in budgetreader: 

        # Append the months and the P&L to their corresponding lists
        months.append(row[0])
        pl.append(int(row[1]))
    
    # Calculate Total Months and Total P&L
    count_months = len(months)
    sum_pl = sum(pl)

    # Using the sum_pl list, go through each month's P&L to get the monthly change
    # Subtract 1 from the total count of the months since Range function starts from 0
    for i in range(count_months -1):
        
        # Take the difference between current month vs. previous month and append to P&L change list
        # i + 1 is the current month while i will be the previous month
        pl_change.append(pl[i+1]-pl[i])
    
    # Calculate the Average Change
    pl_average = round(sum(pl_change)/len(pl_change),2)

    # Calculate the max and min of P&L change and corresponding month
    # Use index to match the P&L change to the month 
    # Add 1 at the end since month associated with change is the next month
    greatest_increase[1] = max(pl_change) 
    greatest_increase_month = pl_change.index(max(pl_change)) + 1
    greatest_increase[0] = (months[greatest_increase_month])
    greatest_decrease[1] = min(pl_change)
    greatest_decrease_month = pl_change.index(min(pl_change)) + 1 
    greatest_decrease[0] = (months[greatest_decrease_month])

    # print results to the terminal
    print("Financial Analysis")
    print("------------------------------------------------------")
    print(f'Total Months: {count_months}')
    print(f'Total: ${sum_pl}')        
    print(f'Average Change: ${pl_average}')
    print(f'Greatest Increase in Profits: {greatest_increase[0]}, (${greatest_increase[1]})')
    print(f'Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})')
      
# create text file with the printed results
with open(budget_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("--------------------------------------------------\n")
    file.write(f'Total Months: {count_months}\n')
    file.write(f'Total: ${sum_pl}\n')
    file.write(f'Average Change: ${pl_average}\n')
    file.write(f'Greatest Increase in Profits: {greatest_increase[0]}, (${greatest_increase[1]})\n')
    file.write(f'Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})\n')
    file.write("--------------------------------------------------\n")


    