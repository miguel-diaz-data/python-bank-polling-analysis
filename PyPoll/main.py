import os
import csv

total_votes = 0
votes = {}
leader = ""
top_votes = 0

# create filepath for budget data file and read csv file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #check if first row was iterated through properly as header isn't part of data
    #print(f"{csv_header}")
    
    for row in csvreader:
    #The total number of votes cast +1
        total_votes += 1

    #will check on each iteration if the name voted for is on the dict so far, and if not add it, if so +=1 votecount
        if (row[2] in votes):
            votes[row[2]] += 1
        else:
            votes[row[2]] = 1

#first line of output string

output = f"Election Results\n----------------------------\nTotal Votes: {total_votes}\n----------------------------"   

#Iterate through the dict of candidates, start \n and append output string with the following:
#List of candidates who received votes   
#The percentage of votes each candidate won
#The total number of votes each candidate won

for candidate in votes.keys():
    output = f"{output}\n{candidate}: {(votes[candidate])/total_votes *100:.3f}% ({votes[candidate]})"
    
    #check if name of candidate is max value of votes
    if votes[candidate]>top_votes:
        leader = candidate
        top_votes = votes[candidate]

#The winner of the election based on popular vote
output = f"{output}\n----------------------------\nWinner: {leader}\n----------------------------"
print(output)

with open("Analysis\\Analysis.txt", "w") as datafile:
    datafile.write(output)

    