#using pybank as refrence code
import os
import csv

total_votes = 0
votes = {}

print(os.getcwd())
# create filepath for budget data file and read csv file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #checked if first row was iterated through properly as header isn't part of data
    #print(f"{csv_header}")
    
    for row in csvreader:
        print(row)
    #The total number of votes cast +1
        total_votes += 1

    #will check on each iteration if the name voted for is on the dict so far, and if not add it, if so +=1 votecount
        if (row[2] in votes):
            votes[row[2]] += 1
        else:
            votes[row[2]] = 1
    #A complete list of candidates who received votes
    
print(votes.keys())

#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote. 
#get the max value from list of votes

#output = f"Election Results\n----------------------------\nTotal Votes: {total_votes}"
#loop through dict to add each candidate's name and votecount be appended to the output string
#output += \n----------------------------\Winner: {max value from dict}
#print(output)

#with open("Analysis\Analysis.txt", "w") as datafile:
    #datafile.write(output)

    