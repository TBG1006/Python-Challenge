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
    months = []
    profitData = [] 
    monthProfitChange = []

    # iterate through columns in csv and add to lists
    for row in csvreader:
        
        #add months to totalMonths
        months.append(row[0])

        #add P/l data to profitData 
        profitData.append(int(row[1]))
    #print(Months)
    #print(profitData)

    #Find number of months 
    totalMonths = len(months)
    #print(totalMonths)

    # add profit change data to list 
    for i in range(len(profitData)-1):
        monthProfitChange.append(profitData[i+1]-profitData[i])
    
    # function to find average
    def Average(monthProfitChange):
        return sum(monthProfitChange) / len(monthProfitChange)

    #call function to find average
    averageProfit = round(Average(monthProfitChange),2)
    #print(averageProfit)

    # find max profit in list
    maxProfitChange = max(monthProfitChange)
    #print(maxProfitChange)

    # find min profit in list
    minProfitChange = min(monthProfitChange)
    #print(minProfitChange)

    # find index value of max profit to pass into months[] add one because we have to use the monthe we are subtracting FROM
    maxMonth = monthProfitChange.index(max(monthProfitChange)) +1
    #print(maxMonth)

    # find index value of min profit to pass into months[] add one because we have to use the monthe we are subtracting FROM
    minMonth = monthProfitChange.index(min(monthProfitChange)) +1

    #  This section prints values to terminal #####
    
    print("Financial Anlaysis:")
    print("----------------------------------------------")
    print(f"Total Months: {len(totalMonths)}")
    print(f"Net Total P/L: ${sum(profitData)}")
    

