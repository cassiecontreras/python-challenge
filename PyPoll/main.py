    #Create a Python script that analyzes the votes and calculates each of the following:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote

    #Import dependencies
import os
import csv
import collections
from collections import Counter

    #Define variables
voters_candidates = []
votes_per_candidate = {}
percent_candidate_votes = {}
candidate_votes = {}
total_votes = 0
winner_count = 0
winner = ""

    #Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

    #Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

    #Open the CSV
with open(election_data_csv_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvfile)

     # Loop through looking for candidates
        for row in csv_reader:
            total_votes = total_votes + 1
        
        #list of candidates who received votes 
if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
else:
            candidate_votes[row[2]] = 1

    #percentage of votes each candidate won
for key, value in candidate_votes.items():
            percent_candidate_votes[key] =round((value/total_votes)* 100 , 3)


if percent_candidate_votes[key] > winner_count:
                winner_count = candidate_votes[key]
                winner = key
                
          
    
#print the result on terminal    
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for key, value in candidate_votes.items():
    print(key,':' , str(percent_candidate_votes[key]),'%','  ','(',candidate_votes[key],')')
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Export a text file with the results
election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:
    outfile.write(f"Election Results\n")
    outfile.write(f"-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for key, value in candidate_votes.items():
        outfile.write(f"{key}: {str(percent_candidate_votes[key])}%   ({candidate_votes[key]})\n")
    outfile.write(f"-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write(f"-------------------------\n")