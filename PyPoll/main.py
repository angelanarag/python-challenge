# Analyze and calculates the following using the election_data.csv file
#  - Total number of votes cast
#  - Complete list of candidates who received votes
#  - The percentage of votes each candidate won
#  - The total number of votes each candidate won
#  - The winner of the election based on popular vote

# Import the modules
import os
import csv

# Set file path to budget_data.csv 
election_file = os.path.join("Resources", "election_data.csv")

# Set output of the file
election_output = os.path.join("analysis", "election_output.txt")

# Set variables
total_votes = 0
candidate_1 = ["", 0, 9999999]
candidate_2 = ["", 0, 9999999]
candidate_3 = ["", 0, 9999999]

# Open the csv file
with open(election_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    electionreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(electionreader)

    # Read each row of data after the header
    for row in electionreader:
    
        # Count the votes
        total_votes += 1

        # Count the votes each candidate received

# print results
print("Election Results")
print("------------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------------------------------")

# write results to a text file
with open(election_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("--------------------------------------------------\n")
    file.write(f'Total Months: {total_votes}\n')
    file.write("--------------------------------------------------\n")