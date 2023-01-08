# -------------------------------------------
# WRONG AVERAGE CHANGE RESULTS
# -------------------------------------------
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

total_months = 0
total_pl = 0
pl = []
prev_pl = 0
month_of_change = []
pl_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
pl_change_list = []
pl_average = 0

# Open the csv file
with open(budget_file) as csvfile:

    # Specify delimiter and variable that holds contents of the csv file
    budgetreader = csv.reader(csvfile, delimiter=',')
    # budgetreader = csv.DictReader(csvfile)

    # Read the header row first and skip to next so you don't include it in the count
    csv_header = next(budgetreader)

    # Read each row of data after the header
    for row in budgetreader:
    
        # Count the months
        total_months += 1
        
        # Calculate the total profit loss
        total_pl = total_pl + int(row[1])
        
        # Calculate average change
        # Take the current month's p&l and subtract the previous month's p&l for p&l change 
        pl_change = int(row[1]) - prev_pl
        prev_pl = int(row[1])
        # Save each p&l change from month to month in a list 
        pl_change_list = pl_change_list + [pl_change]
        month_of_change = [month_of_change] + [row[0]]

        # Find the greatest increase in p&l change and the corresponding month
        if pl_change > greatest_increase[1]:
            # Places the greatest increase p&l changes in the second position
            greatest_increase[1] = pl_change
            # Places the corresponding month in the first position
            greatest_increase[0] = row[0]

        # Find the greatest decrease in p&l change and the corresponding month
        if pl_change < greatest_decrease[1]:
            greatest_decrease[1] = pl_change
            greatest_decrease[0] = row[0]
        
        # Once script has gone through all the rows, you will have a list of all p&l changes
        # As well as the greatest increase and greatest decrease in p&l change 

    # Calculate average p&l by summing all the p&l changes and dividing by the count
    pl_average = round(sum(pl_change_list)/len(pl_change_list), 2)

# print results to the terminal
print("Financial Analysis")
print("------------------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_pl}')
print(f'Average Change: ${pl_average}')
print(f'Greatest Increase in Profits: {greatest_increase[0]}, (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})')
        


# create text file with the printed results
with open(budget_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("--------------------------------------------------\n")
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${total_pl}\n')
    file.write(f'Average Change: ${pl_average}\n')
    file.write(f'Greatest Increase in Profits: {greatest_increase[0]}, (${greatest_increase[1]})\n')
    file.write(f'Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})\n')
    
# END