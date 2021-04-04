import os
import csv

csvpath = os.path.join('PyBank', 'Resources', 'PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Set lists to accept data from csv
    totalMonths = []
    netTotal = []
    profitData = [] 

    # iterate through columns in csv and add to lists
    for row in csvreader:
        
        #add months to totalMonths
        totalMonths.append(row[0])

        #add P/l 
        profitData.append(int(row[1]))


    print(totalMonths)

    print(profitData)