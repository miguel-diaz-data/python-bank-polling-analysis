#using pybank as refrence code
import os
import csv

total_votes = 0

print(os.getcwd())
# create filepath for budget data file and read csv file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #checked if first row was iterated through properly as header isn't part of data
    #print(f"{csv_header}")
    
    for row in csvreader:

    #The total number of votes cast +1
    total_votes += 1

#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote. 
 
#output = f"Financial Analysis\n----------------------------\nTotal Months: {total_months} \nTotal: ${abs_change}\nAverage Change: ${avg_change:.2f}\n" + max_profit_str +"\n" + max_loss_str
#print(output)

#with open("Analysis\Analysis.txt", "w") as datafile:
    #datafile.write(output)

    