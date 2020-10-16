import os
import csv

total_months = 0
delta = 0
total_changes = 

# create filepath for budget data file and read csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    print(f"{csv_header}")
    #checked if first row was iterated through properly as header isn't part of data

    for row in csvreader:
#The total number of months included in the dataset
#can be done through looping and counting the number of iterations. or len function if it exists
        total_months += 1
#The net total amount of "Profit/Losses" over the entire period
        delta = int(row(1))
#can be done through reading the second column and converting to int, removing any - signs and adding it all up

#The average of the changes in "Profit/Losses" over the entire period
#can be done through adding all the changes, without removing the - signs, and dividing the sum by total numnber of months in dataset

#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#can be done by keeping a running min and max variable and comparing it with the current one. 





