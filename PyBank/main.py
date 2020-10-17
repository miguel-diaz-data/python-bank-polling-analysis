import os
import csv

total_months = 0
delta = 0
abs_change = 0
net_change = 0
max_loss = 0
max_loss_str = ""
max_profit = 0 
max_profit_str = ""

# create filepath for budget data file and read csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #checked if first row was iterated through properly as header isn't part of data
    #print(f"{csv_header}")
   
    for row in csvreader:
    #Counts the total number of months included in the dataset
        total_months += 1

        delta = int(row[1])
    #Uses current row value to update total amount of "Profit/Losses" over the entire period

        abs_change += abs(delta)

    #Uses current row value to update the net change needed to calculate the average change
        net_change += delta
        
    #checks if current row has max/min value so far
    #also update the str with the required output
        if int(row[1]) > max_profit:
            max_profit = int(row[1])
            max_profit_str = f"Greatest Increase in Profits: {row[0]} (${row[1]})"
        elif int(row[1]) < max_loss:
            max_loss = int(row[1])
            max_loss_str = f"Greatest Decrease in Profits: {row[0]} (${row[1]})"


avg_change = net_change/total_months
 
output = f"Financial Analysis\n----------------------------\nTotal Months: {total_months} \nTotal: ${abs_change}\nAverage Change: ${avg_change:.2f}\n" + max_profit_str +"\n" + max_loss_str
print(output)

with open("Analysis\Analysis.txt", "w") as datafile:
    datafile.write(output)

    

