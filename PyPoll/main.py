#Create a file path across operating systems
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Read the header row
    csv_header = next(csvreader)

    # Initialize variables for total votes, candidate votes, and winning candidate
    total_votes = 0
    candidate_votes = {}
    winning_candidate = ""
    winning_candidate_votes = 0
    candidate_name = ""

    # Loop through each row in the CSV file
    for row in csvreader:

        # Calculate the total votes
        total_votes += 1

        # List of candidates, total votes and percentage of each candidate won
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

        # The winner of the election based on the highest number of votes
        if candidate_votes[candidate_name] > winning_candidate_votes:
            winning_candidate = candidate_name
            winning_candidate_votes = candidate_votes[candidate_name]

    #Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        percentage_votes = (votes / total_votes) * 100
        print(f"{candidate}: {percentage_votes:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print("-------------------------")

#set as text file
txtpath ='Analysis/election_results.txt'
with open(txtpath, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage_votes = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {percentage_votes:.3f}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winning_candidate}\n")
    text_file.write("-------------------------\n")
    


