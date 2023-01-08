# Analyze and calculates the following using the election_data.csv file
#  - Total number of votes cast
#  - Complete list of candidates who received votes
#  - The percentage of votes each candidate won
#  - The total number of votes each candidate won
#  - The winner of the election based on popular vote

# Import the modules
import os
import csv

# Set file path to election_data.csv 
election_file = os.path.join("Resources", "election_data.csv")

# Set output of the file
election_output = os.path.join("analysis", "election_output.txt")

# Set variables
total_votes = 0
each_candidate_votes = 0
candidates = []
votes = {}
winner_votes = 0


# Open the csv file
with open(election_file) as csvfile:

    # Specify delimiter and variable that holds contents of the csv file
    electionreader = csv.reader(csvfile, delimiter=',')

    # Read and skip the header row 
    csv_header = next(electionreader)

    # Read each row of data after the header
    for row in electionreader:
    
        # Count the total votes
        total_votes += 1

        # Indicate where to find the candidate name
        candidate_name = row[2]
        # Count the votes each candidate received
        # Check if the candidate is already in the list
        if candidate_name not in candidates:
            # if the name is not on the list, add it
            candidates.append(candidate_name)
            # for each candidate, record one vote
            votes[candidate_name] = 1
        
        # Once all the candidates are on the list, the program will continue to go through all the rows
        #   and add the votes for each candidate
        votes[candidate_name] = votes[candidate_name] + 1
    
    # Calculate the percentage of votes each candidate won
    for candidate_name in votes:
        # set new variable for each candidate's votes so we can compare
        each_candidate_votes = votes[candidate_name]
        # set new variable for percentage votes for each candidate
        vote_percent = round((each_candidate_votes)/(total_votes)*100, 2)
        # find the winner by comparing the votes
        if (each_candidate_votes > winner_votes):
            # Since winner_votes = 0 at beginning of program, first candidate will be the winner
            winner_votes = each_candidate_votes
            winner = candidate_name
            # And as the program goes through each candidate on the list, a new winner will be set
        
        # Set-up the string to show candidate, percentage vote and votes
        candidate_output = f"{candidate_name}: {vote_percent}% {each_candidate_votes}\n" 





# print results
print("Election Results")
print("------------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------------------------------")
print(candidate_output)
print("------------------------------------------------------")
print(f'{winner}:  {winner_votes}')


# write results to a text file
with open(election_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("--------------------------------------------------\n")
    file.write(f'Total Months: {total_votes}\n')
    file.write("--------------------------------------------------\n")
    file.write(f'{candidate_output}\n')
    file.write(f'{winner}:  {winner_votes}')