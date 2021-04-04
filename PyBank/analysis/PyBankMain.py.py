import os
import csv

csvpath = os.path.join('PyBank', 'Resources', 'PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    netTotal = 0 

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        # calculate total number of months
        totalMonths =  len(list(csvreader))
        # calc net total profit/loss 
        netTotal += int(row[1])

print(f"Net Total P/L: {netTotal}")
print(f"Total Months: {totalMonths}")

    #print(row)
